## torch2onnx
1. torch转onnx，存在变量时转模型失败
    - 进入..envs\torch\lib\site-packages\torch\onnx\symbolic_helper.py, 在提示位置print(v.node())查看转模型失败的位置

    - 转模型不可用：

        ```
        avg = F.avg_pool2d(feat32, feat32.size()[2:])
        ```
    - 转模型可用：
        ```
        avg = F.avg_pool2d(feat32, 16)
        ```
        ```
        self.avg = nn.AvgPool2d(16)
        ...
        x = self.avg(x)
        ```
    - 同理Max和Avg和Adaptive_*中，根据输入size修改