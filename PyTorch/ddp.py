import torch
import torch.nn as nn
import argparse
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader
import os
from torch.utils.data.distributed import DistributedSampler
 
# 1)**********设置参数local_rank**********************************************
parser = argparse.ArgumentParser()
parser.add_argument('--local_rank', default=-1, type=int,
                    help='node rank for distributed training')
args = parser.parse_args()
 
# 通过args接收 local_rank
local_rank = args.local_rank
 
# 通过 get_rank() 得到 local_rank，最好放在初始化之后使用
local_rank = torch.distributed.get_rank()
 
# 2)****************使用nccl后端****************************************
torch.distributed.init_process_group(backend="nccl")
 
# 3)******************配置每个进程的gpu**************************************
# 获取 local_rank
local_rank = torch.distributed.get_rank()
#配置每个进程的 GPU， 根据local_rank来设定当前使用哪块GPU
torch.cuda.set_device(local_rank)
device = torch.device("cuda", local_rank)
 
# 4)********************数据集分发************************************
# 自己的数据获取
dataset = MyDataset(input_size, data_size)
 
# 使用 DistributedSampler， pin_memory=True , batchsize是每个进程的batchsize
train_sampler = torch.utils.data.distributed.DistributedSampler(dataset)
 
trainloader = DataLoader(dataset=dataset,
                         pin_memory=True,
                         shuffle=(train_sampler is None),   # 使用分布式训练 shuffle 应该设置为 False
                         batch_size=args.batch_size,
                         num_workers=args.workers,
                         sampler=train_sampler)
 
 
 
# 5)**************************DDP******************************
model = Model()
# 把模型移到对应的gpu
# 定义并把模型放置到单独的GPU上，需要在调用`model=DDP(model)`前做
model.to(device)
 
# 引入SyncBN，这句代码，会将普通BN替换成SyncBN。
model = torch.nn.SyncBatchNorm.convert_sync_batchnorm(model)
 
# GPU 数目大于 1 才有必要分布式训练
if torch.cuda.device_count() > 1:
    model = torch.nn.parallel.DistributedDataParallel(model,
                                                      device_ids=[local_rank],
                                                      output_device=local_rank)
 
 
# 6)********************************************************
 
for epoch in range(num_epochs):
    # 设置sampler的epoch，DistributedSampler需要这个来维持各个进程之间的相同随机数种子
    trainloader.sampler.set_epoch(epoch)
    # 后面这部分，则与原来完全一致了。
    for data, label in trainloader:
        prediction = model(data)
        loss = loss_fn(prediction, label)
        loss.backward()
        optimizer = optim.SGD(ddp_model.parameters(), lr=0.001)
        optimizer.step()