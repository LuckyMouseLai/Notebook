2022.12.11
onnx 1.13即将发布

function op、parser、training 支持、reference runtime、onnx hub 等

## 新特性-training支持

## 新特性-onnx hub-在线加载模型
    - onnx的模型仓库
    ```
    from onnx import hub
    ## 获得resnet50 onnx预训练模型
    model = hub.load('resnet50')
    ## 列出onnx/models所有模型
    all_models = hub.list_models()
    ## 列出指定模型的所有versions/opsets
    mnist_models = hub.list_models(model='mnist')
    ## 列出所有匹配tag的模型
    vision_models = hub.list_models(tags=['vision'])
    ```
## 新特性-parser
    - 从文本格式解析为一个网络模型
## 新特性-function op
    - 会给onnx带来根本性变革的特性
    - onnx包含的算子越来越多，后端支持的成本也越来越大
    - function op是一种可以分解为多个小算子的算子。当使用一个未知功能算子时，可以利用已有的算子结合起来实现。大大减小后端对算子的适配成本
## 新特性-reference runtime
    - 只依赖python和numpy
    - 不需要安装onnxruntim
    - verbose=1，一键输出所有中间数据，主要用于debug,不适用线上，线上使用onnxruntime/trt
```
from onnx.reference import ReferenceEvaluator
sess = ReferenceEvaluator('model.onnx', verbose=1)
```

## onnxsim
- 功能 - 自动优化onnx模型
    2. 动态输入形状
    3. 自定义OP
    4. >2GB大模型
    5. 形状推到+图变换+常量折叠

## onnx-modifier-可视化模型修改工具
    - 添加/删除算子
    - 重命名算子输入/输出
    - 修改算子属性
    - 修改模型batchsize
    - 修改模型权重

## PPQ量化工具
    - onnx量化 sota 首推工具
