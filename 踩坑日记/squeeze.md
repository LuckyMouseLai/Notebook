## squeeze
## 问题描述. 

batchsize为1时使用squeeze报错。或者在第一轮训练结束时报错。

## 问题分析和解决办法
    ```
    import torch

    input_data = torch.ones(1, 3, 299, 299)  # batch为1的输入，shape=(1, 3, 299, 299)
    mid_features = torch.reshape(input_data, (1, 3, 1, 299*299))  # 中间层数据变化, shape=(1, 3, 1, 299*299)

    squeeze_data1 = torch.squeeze(mid_features)  # squeeze，不指定压缩维度，shape=(3, 299*299)
    squeeze_data2 = torch.squeeze(mid_features, dim=2) # squeeze，指定压缩维度，shape=(1, 3, 299,299)
    ```

1. 在模型forward中使用squeeze，当batchsize为1的时候，会将数据的第一维去除(如squeeze_data1)，导致报错。
解决方法：指定压缩维度，如squeeze_data2

2. 并不意味着batchsize设为1才会出现这种情况。当你的最后一个batch为1的时候，也就是数据集总数n/batchsize，余数为1，也会报错，但是这种在刚开始训练时不会报错，在第一个epoch的最后一个batch才会报错。
解决方法：修改batchsize，使得余数不为1，不建议，影响训练。可在dataloader加载时设置drop_last=True，丢弃最后一个batch。
    ```
    torch.utils.data.DataLoader(image_datasets,
                batch_size=args.batch_size,
                shuffle=True, 
                num_workers=args.num_workers,
                drop_last=False)
    ```
    

    
