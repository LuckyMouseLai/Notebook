# 数据增广
1. torchvision.transforms
    ```
    trans = transforms.Compose([
            transforms.Resize((self.args.image_size, self.args.image_size)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
    aug_img = trans(image)
    ```
    - 输入为image格式为PIL的Image格式
    - totensor在normalize前
2. albumentations

    ```
    import albumentations as A
    from albumentations.pytorch import ToTensorV2

    trans = A.Compose([
        A.HorizontalFlip(p=0.5),
        A.RandomBrightnessContrast(p=0.3),
        A.ImageCompression(p=0.3, quality_lower=10, quality_upper=30),
        A.HueSaturationValue(hue_shift_limit=(-0.3,0.3), sat_shift_limit=(-0.3,0.3), val_shift_limit=(-0.3,0.3), p=0.3),
        A.Resize(args.image_size, args.image_size),
        A.Normalize(mean=(0.5, 0.5, 0.5), std=(0.5, 0.5, 0.5)),
        ToTensorV2(),
    ])
    aug_img = trans(image=image)['image']
    # -----------------------------------
    augs = trans(image=image, mask=mask)
    aug_img, mask = augs['image'], augs['mask']
    ```
    - 输入格式nparray, 一般使用cv2.imread读取后从BGR转为RGB在输入trans
    - 先normalize在totensor
    - 使用时参数名称不可少'image=' 'mask='
    - 使用mask，适用于类似图像分割，同步resize，翻转等操作，不会对mask进行图像压缩等增广