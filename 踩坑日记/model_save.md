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