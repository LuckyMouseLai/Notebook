# 分布式训练
1. 单机单卡
    ```
    import os
    os.environ["CUDA_VISIBLE_DEVICES"] = "1, 2, 0"
    ...
    model.to('cuda:0')  # 0表示序号，因可用gpu序列设置为[1,2,0]，所以model在device 1上
    ```
2. 单机多卡-DataParallel
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
3. 单机多卡/多机多卡-torch.nn.parallel.DistributedDataParallel
- 未使用过
