# locals and globals

1. locals()- 以字典形式返回当前全部局部变量
    ```
        d = 5
        def fun1(nums=0):
            a = 1
            b = nums+1
            print(locals())  # 当前局部变量 a,b,nums
        def fun2():
            c = 3
            
            return c
        fun1()
    ```
    返回值：
    ```
        {'nums': 0, 'a': 1, 'b': 1}
    ```
    利用locals运行函数fun2
    ```
        d = 5
        def fun1(nums=0):
            a = 1
            b = nums+1
        def fun2(c):

            return c
        locals()['fun2'](4)  # 返回4
    ```

2. globals()-同locals，但返回全局变量