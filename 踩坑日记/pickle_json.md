## pickle和json
1. pickle和json的差异
    - pickle模块只能对python的数据结构序列化(python所有的数据类型包括类和函数)
    - json适用于多平台多语言的字符串与python数据类型转换，支持python的数据类型有str,tuple,list,dict,set
    - pickle和json同样有loads,load, dumps,dump函数，功能类似
2. json
    - json.loads(): 把str, byte, bytearray转化为python对象-字典
    - json.load(): 读取json文件
    - json.dumps(): python对象转为json对象，例如：字典转为字符串
    - json.dump: 写入json文件，即保存为json

    ```
    print('--------------loads--------------------')
    ## json.loads  str, byte, bytearray转化为python对象-字典
    s = '{"data": "123.png", "label": "1"}'
    result = json.loads(s)
    print(type(s), type(result))
    print(result)
    print('--------------load--------------------')
    ## json.load  读取json文件
    with open('/home/Users/lzq/tensorflow-mnist/app.json', 'r') as f:
        result = json.load(f)
        print(type(f), type(result))
        print(result)
    print('--------------dumps--------------------')
    ## json.dumps   python对象转为json对象，例如：字典转为字符串
    s = {"data": "123.png", "label": "1"}
    result = json.dumps(s)
    print(type(s), type(result))
    print(result)
    ## json.dump  写入json文件，即保存为json
    # with open('./test_json.json', 'w') as f:
        # s = {"data": "123.png", "label": "1"}
        # json.dump(s, f)
    ```
    ```
    --------------loads--------------------
    <class 'str'> <class 'dict'>
    {'data': '123.png', 'label': '1'}
    --------------load--------------------
    <class '_io.TextIOWrapper'> <class 'dict'>
    {'name': 'tensorflow-mnist', 'buildpacks': [{'url': 'https://github.com/heroku/heroku-buildpack-nodejs'}, {'url': 'https://github.com/heroku/heroku-buildpack-python'}]}
    --------------dumps--------------------
    <class 'dict'> <class 'str'>
    {"data": "123.png", "label": "1"}
    ```