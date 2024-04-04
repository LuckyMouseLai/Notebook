## torch2onnx
1. torch2onnx
    - 转模型
    ```
    device = torch.device('cpu')
    modelpath = './checkpoints/yolov7.pt'
    ## 定义模型并加载权重
    model = MyModel().to(device)
    state_dict = torch.load(modelpath)
    model.load_state_dict(state_dict, strict=True)
    model.eval()
    ## 设置模型输入和输出名称
    input_names = ['input_0']
    output_names= ['output_0']
    input = torch.ones(1,3,512,512).to(device)  
    ## 转换后onnx保存路径
    savepath = './yolov7.onnx'
    ## 模型转换，其中dynamic_axes指定输入输出维度可动态变化，不指定在推理时输入维度需和input一致，这里的话第2,3维度即宽高可变。
    torch.onnx.export(model, input, savepath, export_params=True,
                      verbose=True, output_names=output_names,
                      input_names=input_names, opset_version=11, dynamic_axes={'input_0':[2,3], 'output_0':[2,3]})
    ```
    - 推理
    ```
    ## 定义推理会话
    session = onnxruntime.InferenceSession('./yolov7.onnx', providers=['CPUExecutionProvider'])  # 使用cpu
    # self.session = onnxruntime.InferenceSession('./yolov7.onnx', providers=['CUDAExecutionProvider'])  # 使用gpu
    ### 数据处理过程省略
    image = image.unsqueeze(0)
    ## 推理，注意输入和输出名称需要同转模型时一致。可通过session.get_inputs()和session.get_outputs()或通过onnx加载查询。
    pred = self.session.run(output_names=['output_0'], input_feed={'input_0': image.numpy()})
    ```
2. torch转onnx，存在动态非tensor变量时转模型失败
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