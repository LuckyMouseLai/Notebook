# 分布式训练
1. 单机单卡
    ```
    import os
    os.environ["CUDA_VISIBLE_DEVICES"] = "1, 2, 0"
    ...
    model.to('cuda:0')  # 0表示序号，因可用gpu序列设置为[1,2,0]，所以model在device 1上
    ```
2. 单机多卡-DataParallel
    - forward：复制模型到多个GPU上，数据按batchsize分发到多个GPU，forward计算，结果输出聚合到主GPU
    - backward: 主GPU计算损失，将损失值分散给各个GPU，每个GPU反向传播计算梯度，梯度聚合在主GPU上进行梯度下降，更新梯度
    - DataParallel是单进程多线程，不是真正意义的并行，所有GPU计算完了才进行梯度更新
    - 缺点：计算慢、GPU负载不均衡
    ```
    import os
    os.environ["CUDA_VISIBLE_DEVICES"] = "0, 1, 2"  # 设置可用设备
    ...
    device_ids = [1, 2, 0]  # 使用的设备
    model= torch.nn.DataParallel(model, device_ids=device_ids, output_device=0)
    model = model.cuda()
    ```
    - device_ids: 使用的gpu
    - output_device: 输出结果的设备，所以该设备使用显存更多一点，默认device_ids[0], 代码中的device 1
    - 使用DataParallel训练，精度比单gpu训练略低, 显存分配不平衡。并且模型中的名称变为nn.module, 因此加载模型需修改：
    ```
    ### load weights
    state_dict = torch.load(model_path)
    model_state_dict = model.state_dict()
    for k, v in model_state_dict.items():
        name = 'module.' + k
        model_state_dict[k] = state_dict[name]
    model.load_state_dict(model_state_dict)
    ```
    ```
    model = torch.nn.DataParallel(model)
    state_dict = torch.load(model_path)
    model.load_state_dict(state_dict)
    ```
    ```
    if isinstance(model, DistributedDataParallel):
        model = model.module

    model.load_state_dict(checkpoint))
    ```
3. 单机多卡/多机多卡-torch.nn.parallel.DistributedDataParallel
    - MPI实现CPU通信，NCCL实现GPU通信
    - 一份代码，自动分配n个进程，分别在n个GPU上运行，每个GPU执行相同的任务，各个进程间加载的数据不重叠
    - 优点：速度快，效率高
    - 每个进程相当于单独的训练，每个进程有自己的optimizer，初始化时进行一次广播，使各进程中的初始参数一致。forward过程各自进行，backward过程各自进行(前向和反向同正常训练一致)，此时，将计算的梯度进行汇总平均，由rank=0的进程，广播到所有进程，实现所有进程中梯度一致，由各个进程执行梯度下降更新参数。仅仅在梯度汇总时进行信息交换。因此，速度快，效率高
    - 概念：rank表示进程号，local_rank表示gpu号
    - 代码，见../PyTorch/ddp.py
    - ddp启动
        1.  torch.distributed.launch
        ```python -m torch.distributed.launch --nproc_per_node=4 main.py --{args}```
        2. torch.multiprocessing
        ```
        import torch.multiprocessing as mp
        def main(rank, your_custom_arg_1, your_custom_arg_2):
            pass # 将前面那一堆东西包装成一个 main 函数
        mp.spawn(main, nprocs=how_many_process, args=(your_custom_arg_1, your_custom_arg_2))
        ```
        
