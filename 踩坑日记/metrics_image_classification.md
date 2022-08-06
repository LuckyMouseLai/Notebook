# 评价指标-metrics

1. test阶中，多次测试的准确率不一致
    - 没有使用model.eval(), 导致模型中BN和Dropout没有关闭
        ```
        model.eval()
        with torch.no_grad():
            ...
            outputs = model(data)
            ...
        ```
    - 数据层面上，加载数据集是drop_last设置为true，并且数据总数/batchsize有余数。因此test数据集的drop_last应设为false。
        ```
        torch.utils.data.DataLoader(image_datasets,
                    batch_size=args.batch_size,
                    shuffle=True, 
                    num_workers=args.num_workers,
                    drop_last=False)
        ```
