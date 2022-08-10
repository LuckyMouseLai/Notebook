# 自动混合精度

1. 使用自动混合精度计算，降低显存使用(image2image训练中降低明显)，从而可以使用更大的batch size和image size
    - 降低显存：训练时一般是单精度float32计算，使用混合精度，既使用单精度和半精度float16计算。
    - 加速训练和推理
    - 存在舍入误差，因为使用了半精度，其精度表示没有单精度广。
    - 使用Scaler来解决fp16梯度underflow问题。训练时梯度过小，会变为0，所以对loss放大，因为链式法则，放大后的会平移到fp16的有效位。
    
2. 使用方式 autocast(torch>1.6) + GradScaler
    - 在模型forward前加上装饰器autocast()
        ```
        from torch.cuda.amp import autocast
            class Model(nn.Module):
                def __init__(self, model_name, n_class):
                    super().__init__()  
                    self.model = smp.UnetPlusPlus(...)
                @autocast()
                def forward(self, x):
                    ...
                    return x
        ```
    - 反向传播
        ```
        from torch.cuda.amp import autocast, GradScaler

        scaler = GradScaler()
        for epoch in range(10):
            for batch_idx, datas in enumerate(train_dataloader):
                with autocast():
                    loss = criterion(...)
                scaler.scale(loss).backward()
                scaler.step(optimizer)
                scaler.update()
                optimizer.zero_grad()
        ```