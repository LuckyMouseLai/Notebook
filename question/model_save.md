# 模型保存
1. 仅保存模型的权重
    ```
        ## 保存模型
        torch.save(model.state_dict(), './test.pth.tar')
        ## 读取权重文件
        state_dict = torch.load('./test.pth.tar')
        model.load_state_dict(state_dict)
    ```
2. 保存多种信息

    ```
        state = {
            'epoch': epoch +1,
            'state_dict': model.state_dict(),
            'acc': train_acc,
            'best_acc': best_acc,
            'best_epoch':, best_acc_epoch,
            'optimizer', optimizer.state_dict(),
        }
        ## 保存
        torch.save(state, './test.pth.tar')
        ## 读取文件
        state = torch.load('./test.pth.tar')
        state_dict = state['state_dict']  # 权重
        best_acc = state['best_acc']  # best acc
        model.load_state_dict(state_dict)
    ```
3. torch.save()保存整个模型及其加载torch.load()
    - 保存整个模型及其权重文件，在load加载时即得到模型，无需再load_state_dict。但无法直接调整网络结构。
    - torch.load中map_location将权重映射到指定设备上
    ```
    model = Model()
    torch.save(model, './test.pt)
    model = torch.load('./test.pt, map_location='cpu')
    print(model)
    ```
    ```
    Model(
        (fc): Linear(in_features=10, out_features=2, bias=True)
    )
    ```
4. model.load_state_dict(state_dict， strict=True)：模型加载权重

    - strict=True, 严格要求state_dict和model中的weights name and weights shape一致
    - strict=False, 只加载weights name一致的权重，但要求weights shape一致。返回mising_keys, unexpected_keys
    ```
    missing_keys, unexpected_keys = model.load_state_dict(state_dict, strict=False)

    输出：missing_keys=['fc3.weight', 'fc3.bias', 'fc2.weight', 'fc2.bias'], unexpected_keys=['fc.weight', 'fc.bias']
    ```
5. pt, pth, pkl
    - 保存的格式, 之间没有太大差别。c++使用pt
    - torch.save()使用pickle来序列化
    - pth转pt使用torch.jit.trace
        ```
        x = torch.ones((1, 3, 224, 224)) # 模型输入shape
        traced_model = torch.jit.trace(model, x)
        traced_model.save('xxx.pt')
        ```