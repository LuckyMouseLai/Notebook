
1. locals and globals， nonlocal, global

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

    3. global:定义全局变量，可以在函数内定义全局变量，只是标记不能赋值

    4. nonlocal：标记非全局、非本地的自由变量，去非本地，非全局的地方找变量，常用闭包

2. 静态方法、实例方法、类方法
    1. 静态方法：
    - 格式：装饰器+statimethod，第一个参数不需要self，可以存在类中
    - 好处：不需要实例化对象即可使用该方法，可以用于打印和获取当前时间
    - 注意：静态方法中不能调用类的方法
    - 调用：类对象调用(类名.静态方法)， 类实例化(a.静态方法)调用
    2. 类方法
    - 格式：装饰器+classmethod，第一个参数约定cls
    - 调用：类对象调用(类名.类方法)， 类实例化(a.类方法)调用
    3. 实例方法
    - 格式 def(self, *args)，第一个的参数约定self
    - 调用：只能通过实例化对象调用
    ```
        def foo(x):
            print "executing foo(%s)"%(x)

        class A(object):
            def foo(self,x):  # 实例方法
                print "executing foo(%s,%s)"%(self,x)

            @classmethod
            def class_foo(cls,x):  # 类方法
                print "executing class_foo(%s,%s)"%(cls,x)

            @staticmethod
            def static_foo(x):  # 静态方法
                print "executing static_foo(%s)"%x

        a=A()
    ```


3. 类变量和实例变量
    - 类变量，所有实例对象共享，实例变量由各个实例对象独有
    ```
        class Test(object):  
            num_of_instance = 0  
            def __init__(self, name):  
                self.name = name  
                Test.num_of_instance += 1  
  
    if __name__ == '__main__':  
        print Test.num_of_instance   # 0
        t1 = Test('jack')  
        print Test.num_of_instance   # 1
        t2 = Test('lucy')  
        print t1.name , t1.num_of_instance  # jack 2
        print t2.name , t2.num_of_instance  # lucy 2
    ```





4. 列表推导和字典推到
    ```
        l = [value for value in iterable]
        d = {key: value for (key, value) in iterable}
    ```

5. __和_，双下划线和单下划线
    1. __foo:一种约定,用来指定变量私有，只能类本身访问.用来指定私有变量的一种方式.使用 from a_module import * 导入时，这部分变量和函数不会被导入。不过值得注意的是，如果使用 import a_module 这样导入模块，仍然可以用 a_module._some_var 这样的形式访问到这样的对象
    2. __foo__:一种约定,Python内部的名字,用来区别其他用户自定义的命名,以防冲突，就是例如__init__(),__del__(),__call__()这些特殊方法
    3. _foo, protected类型，只能本身和子类访问，不能用于from a_module import *

6. 迭代器和生成器，yield(**)
    1. 概念
        - 可迭代，可通过for遍历，如list，dict，迭代器，生成器，元组， set等
        - 迭代器，指可以记住自己遍历位置的对象，直观体现便是可以使用next()函数返回值，迭代器只能往前，不能往后，当遍历完毕后，next(iteror)会抛出一个StopIteration异常
        - 生成器：指使用yield的函数，生成器也是只能往前，不能往后，当遍历完毕后，next(iteror)会抛出一个StopIteration异常
        - 可迭代＞迭代器＞生成器
        - 迭代器和生成器，均可以通过next(obj)的方式不断返回下一个值
        - 可迭代的对象（包括生成器），均可以通过iter(obj)，转化为迭代器
    2. 生成器和迭代器
        - 迭代器是个类，需要实现__iter__和__next__魔法函数，语法相对来说较为冗余
        - 生成器是个使用yield的函数，相较而言，代码会更加少
        - 在同一代码内，生成器只能遍历一次
        - 迭代器通过iter()创建，next()访问下个元素
    3. for in循环原理：实现了__getitem__()，循环自动调用该函数，实现__iter__会自动忽略getitem
        - 可迭代一定能for，能for不一定可迭代，例如实现了__getitem__
    4. 可迭代对象是一个实现了__getitem__或__iter__的类
    5. 迭代器是一个实现了__getitem__或__iter__ + __next__的类。__iter__返回一个迭代器，__next__实现取数
    6. 生成器是一个函数
        - 创建：ge = (x for x in range(10))或者while循环体+yield
        - yield和return
            - 相同：都在函数体内部，可以返回多个值
            - 不同：yield返回生成器，return执行完直接退出，yield执行完挂起等下一次next(),再从挂起点恢复
            - 生成器中，如果没有return，默认执行完毕

7. *args和**kwargs
    1. 不确定你的函数里将要传递多少参数时你可以用*args.例如,它可以传递任意数量的参数，不指定参数名
    2. **kwargs允许你使用没有事先定义的参数名，需要指定参数名传入是字典类型
    3. 混合使用
        ```
            def table_things(titlestring, **kwargs) # 指定参数在前
            def table_things(*args, **kwargs) # *必须在**前
        ```
    4. *解析出来是列表，**解析字典

        ```
            def print_three_things(a, b, c):
                print 'a = {0}, b = {1}, c = {2}'.format(a,b,c)
            mylist = ['aardvark', 'baboon', 'cat']
            print_three_things(*mylist)

            a = aardvark, b = baboon, c = cat
        ```

8. 装饰器(**)
    1. 用于拓展原来函数功能的一种函数
    2. 返回值：函数
    3. 优点：不更改原函数就能增加新的功能,一个函数可以被多个函数装饰，顺序有里到外
    4. 结构：装饰器函数返回本身函数名，内置函数执行指定操作。
        - 注意：如下有A(), B():@A ，此时调用B(params)中的参数传递到其@的A()函数中的inner(params)，inner中的func()就是B()，如果B有参数，func也要传参
        - 定长参数inner(p1,p2)，任意参数inner(*p1, **p2)
        ```
            def A(func):
                def inner(params):
                    print('1') 
                    func()
                    print('2')
                return inner
            @A
            def B():
                print('b')
            B(params)  # 1 b 2
        ```
    5. 类装饰器，@类名，利用init和call

9. __new__和__init__的区别
    1. __new__是一个静态方法,而__init__是一个实例方法.
    2. __new__方法会返回一个创建的实例,而__init__什么都不返回.
    3. 只有在__new__返回一个cls的实例时后面的__init__才能被调用.
    4. 当创建一个新实例时调用__new__,初始化一个实例时用__init__.

10. 魔术方法:魔术方法是在特定时刻自动触发执行的
    1. __new__
        ```(1). 说明：实例化对象方法

            (2). 触发时机：在实例化时触发

            (3). 参数：至少得有一个cls接收当前类，写法为__new__(cls, *args, **kwargs)

            (4). 返回值：必须使用return关键字返回一个对象实例

            (5). 作用：实例化(创建)对象，开辟内存地址空间对象并返回

            (6). 注意：实例化对象是Object类底层实现，其他类继承了Object的__new__才能够实现实例化对象
        ```
    2. __init__
        ```
            (1). 说明：初始化方法，相当于java中的构造方法，在__new__执行后被调用

            (2). 触发时机：初始化对象时触发（区别于__new__实例化时的触发）

            (3). 参数：至少得有一个self接收__new__方法返回的对象，写法为__init__(self, name, age)

            (4). 返回值：无

            (5). 作用：初始化对象的成员

            (6). 注意：使用该方式初始化的成员都是直接写入对象当中，类中无法具有
        ```
    3. __del__
        ```
            (1). 说明：析构魔术方法

            (2). 触发时机：当一块地址空间没有任何指针引用的时候被触发

            在 Python 解释器中，当所有代码程序执行完成则会进行垃圾回收，也叫内存释放，这时就会触发__del__方法

            使用del 对象名显示删除引用关系时，如果此操作将某块地址空间的最后一个引用关系给删除，则会触发__del__方法

            (3). 参数：仅只一个self参数接收对象

            (4). 返回值：无

            (5). 作用：使用完对象时回收资源，没有指针引用的时候会调用，绝大多数时候不需要重写

            (6). 注意：del 对象名不一定会触发当前方法，只有某块地址空间无任何引用时才会触发
        ```
    4. __call__
        ```
            (1). 说明：调用对象函数的魔术方法

            (2). 触发时机：将对象当作函数调用时触发，使用形式为对象名称()，会默认调用__call__函数里的内容

            (3). 参数：至少得有一个self接收对象，剩余参数根据调用时传入的参数决定，写法为__call__(self, args)

            (4). 返回值：根据具体重写逻辑而定

            (5). 作用：将复杂的步骤统一放在该函数内实现，减少调用的步骤，比较方便

            (6). 注意：无
        ```
    5. __str__
        ```
            (1). 说明：当print(对象名)时想看到更多的信息时，可以重写__str__方法，将想要输出的信息放在__str__函数中返回

            (2). 触发时机：使用print(对象名)或者str(对象名)的时候触发

            (3). 参数：一个self参数接收对象

            (4). 返回值：必须是字符串类型

            (5). 作用：print(对象名)时可以自定义输出更多有用信息

            (6). 注意：无

        ```
11. 单例模式(**)
    - 单例模式是指创建唯一对象
    - 创建方法
        1. import 方式：在一个py文件创建一个类，并且实例化。使用时直接import实例化对象
            ```
                # mysingleton.py
                class My_Singleton(object):
                    def foo(self):
                        pass

                my_singleton = My_Singleton()

                # to use
                from mysingleton import my_singleton

                my_singleton.foo()
            ```
        2. 装饰器方式: 在类前使用装饰器，判断类是否实例化，是就返回原来对象，否则创建
            ```
                def singleton(cls):  # cls传入的类
                    instances = {}  # 存放已经实例化的类对象
                    def getinstance(*args, **kw):
                        if cls not in instances:  # 判断该类是否实例化，没有则实例化，有则返回原来的实例化对象
                            instances[cls] = cls(*args, **kw)
                        return instances[cls]
                    return getinstance

                @singleton
                class MyClass:
            ```
        3. 共享属性:创建实例时把所有实例的__dict__指向同一个字典,这样它们具有相同的属性和方法.
            ```     
            class Borg(object):
                _state = {}
                def __new__(cls, *args, **kw):
                    ob = super(Borg, cls).__new__(cls, *args, **kw)
                    ob.__dict__ = cls._state
                    return ob

            class MyClass2(Borg):
                a = 1
            ```
        4. 使用__new__方法,重写__new__，保证只创建一个实例
            ```
                class Singleton(object):
                    def __new__(cls, *args, **kw):
                        if not hasattr(cls, '_instance'):
                            orig = super(Singleton, cls)
                            cls._instance = orig.__new__(cls, *args, **kw)
                        return cls._instance

                class MyClass(Singleton):
                    a = 1
            ```

12. GIL线程全局锁
    - 限制多线程同时执行，保证同一时间只有一个线程执行，所以cython里的多线程其实是伪多线程！，并发，防止多线程争夺同一资源。

    - 所以python里常常使用协程技术来代替多线程，协程是一种更轻量级的线程

13. 进程、线程、协程
    - 进程：一个运行的程序（代码）就是一个进程，没有运行的代码叫程序，进程是系统资源分配的最小单位，进程拥有自己独立的内存空间，所有进程间数据不共享，开销大。
    - 线程：cpu调度执行的最小单位，也叫执行路径，不能独立存在，依赖进程存在，一个进程至少有一个线程，叫主线程，而多个线程共享内存（数据共享，共享全局变量),从而极大地提高了程序的运行效率
    - 协程: 是一种用户态的轻量级线程，协程的调度完全由用户控制。微线程，也称为用户级线程，在不开辟线程的基础上完成多任务，也就是在单线程的情况下完成多任务，多个任务按照一定顺序交替执行 通俗理解只要在def里面只看到一个yield关键字表示就是协程.yield实现

14. 闭包
    - 有外部函数和内部函数
    - 内部函数必须引用外部函数的变量，nonlocal
    - 外部函数返回值是内部函数

15. lambda
    - 函数是一个可以接收任意多个参数(包括可选参数)并且返回单个表达式值的匿名函数
    - 一般用来给filter，map这样的函数式编程服务
    - lambda 参数列表: 表达式
    - 例子：
        > filter(lambda x: x % 3 == 0, [1, 2, 3]) 
        > sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5-x))
        > map(lambda x: x+1, [1, 2,3])

16. map，reduce， filter
    - map(函数, 可迭代序列)，返回一个可迭代对象，函数可以是自定义函数，可以是int，str，abs等等
    - reduce(函数，可迭代序列)，函数必须接收2个参数，因为将序列前2个值传入函数中，计算结果接续和next组合传入，知道结束
    - filter(函数，可迭代序列)函数将传入函数依次作用于序列中的每个元素，返回值为True的元素则保留，False则丢弃，按此规律过滤序列。

16. 拷贝 copy和deepcopy
    ```
        import copy
        a = [1, 2, 3, 4, ['a', 'b']]  #原始对象

        b = a  #赋值，传对象的引用
        c = copy.copy(a)  #对象拷贝，浅拷贝
        d = copy.deepcopy(a)  #对象拷贝，深拷贝

        a.append(5)  #修改对象a
        a[4].append('c')  #修改对象a中的['a', 'b']数组对象

        print 'a = ', a
        print 'b = ', b
        print 'c = ', c
        print 'd = ', d

        输出结果：
        a =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
        b =  [1, 2, 3, 4, ['a', 'b', 'c'], 5]
        c =  [1, 2, 3, 4, ['a', 'b', 'c']]
        d =  [1, 2, 3, 4, ['a', 'b']]

    ```

17. 垃圾回收/内存管理 
    1. 引用计数
        - 每个对象都有object，设置一个引用计数变量，有引用就+1，引用删除就减少，为0就结束
        - 优缺点：简单实时性，循环引用，计数消耗资源
    2. 标记-清除机制
        - 按需分配，等到没有空闲内存的时候从寄存器和程序栈上的引用出发，遍历以对象为节点、以引用为边构成的图，把所有可以访问到的对象打上标记，然后清扫一遍内存空间，把所有没标记的对象释放
    3. 分代技术
        - 将系统中的所有内存块根据其存活时间划分为不同的集合，每个集合就成为一个“代”，垃圾收集频率随着“代”的存活时间的增大而减小，存活时间通常利用经过几次垃圾回收来度量
        - 简言之：按照回收频次划分集合，优先从回收频次高的集合清除
    - 改进：手动垃圾回收，调高回收阈值，避免循环引用

18. 内存泄漏(循环引用，a调b且b调a)
    - 内存泄漏指由于疏忽或错误造成程序未能释放已经不再使用的内存。内存泄漏并非指内存在物理上的消失，而是应用程序分配某段内存后，由于设计错误，导致在释放该段内存之前就失去了对该段内存的控制，从而造成了内存的浪费。
    - 有__del__()函数的对象间的循环引用是导致内存泄露的主凶。不使用一个对象时使用: del object 来删除一个对象的引用计数就可以有效防止内存泄露问题。
    - 避免：sys.getrefcount(obj)获取对象的引用计数，并根据是否为0判断是否泄露

18. 内存溢出
    - 原因：内存中加载数据量过大；集合类对象有对象引用，使用后未清空，使JVM无法回收；存在死循环；启动参数内存设置太小
    - 解决：修改JVM启动参数，查看日志分析代码。

18. is 对比 地址， == 对比 值

19. read, readline, readlines
    1. real: 读取整个文件
    2. readline: 读取下一行，使用生成器方法
    3. readlines: 读取整个文件到一个迭代器，可以用来遍历

20. super和init
    - 在init中用super初始化父类的构造函数init
    - 子类继承父类：子类没有init，可以调用父类；子类init没有super，不可调用父类；子类init且super，可以调用父类
    - 使用父类.__init_时在多继承会调用多次init，使用super不会(MRO)

21. 新式类和经典类
    - MRO，方法解析顺序，处理python二义性问题
    - 二义性：python多继承，A和B类中都有add()，C类继承AB类，调用add时，不知调用哪个
    - 深度优先和广度优先
    - 经典类：
        - 创建时没有继承的类，所有的类型都是type类型，如果经典类作为父类，子类调用父类构造函数会报错
        - 多继承时，使用深度优先
    - 新式类：
        - 新式类是在创建的时候继承内置object对象，子类可以调用基类的构造函数，所有类都有一个公共的祖先类object
        - 多继承时，使用广度优先
        - 加入了静态方法和类方法
        - init改变：
        - 增加new方法：新式类都有一个__new__的静态方法，创建类实例时，会调用类名._new__()，返回实例。还可用于单例模式

22. property
    - 装饰器的方法应用于某个方法,可以调用属性一样来调用方法，变成只读，类实例.func 访问
    - 新式类：@property、@方法名.setter、@方法名.deleter修饰的方法
    - 经典类：只有 @property

23. 多线程
    - 创建方式
        - 通过threading.Thread() 创建
            ```
            import threading
            def test (x,y):
                for i in range(x,y):
                    print(i)
            thread1 = threading.Thread(name='t1',target= test,args=(1,10))
            thread2 = threading.Thread(name='t2',target= test,args=(11,20))
            thread1.start()   #启动线程1
            thread2.start()   #启动线程2
            ```
        - 类继承thread.Thread, 重写run函数
            ```
                import threading
                class mythread(threading.Thread):
                    def run(self):
                        for i in range(1,10):
                        print(i)
                thread1 = mythread();
                thread2 = mythread();
                thread1.start()
                thread2.start()
            ```
    - join(timeout) 阻塞线程，timeout表示阻塞时长，不设置则等待线程结束才解除阻塞
    - run（）：用以表示线程活动的方法
    - start(): 启动线程

    - start（）：启动线程

    - join（）：等待至线程终止

    - isAlive（）：返回线程是否活动的

    - getName（）：返回线程名称

    - setName() : 设置线程名称

24. io密集型和cpu密集型
    - io：cpu性能相对高，cpu处理很快，大部分在等i/o 硬盘内存之间的读写操作
    - cpu：硬盘内存相对cpu性能高，io很短时间结束，主要在等cpu处理运算

25. 可变类型，不可变类型
    - 可变：list，set，dict
    - 不可变：string，int，tuple，不可变集合frozenset
    - 集合类型
        - 创建：{}或set()
        - 无序：没有顺序，元素不能重复，必须是不可变类型
        - 非一致：元素类型可以不同
        - 无索引：遍历或随机取
    - 元组tuple -序列
        - 创建：(,)
        - del删除整个元组，不可变，可索引，可切片
    - 列表-序列
        - 创建：[]
        - 支持不同元素类型，可变，可索引，可切片
    - 字典
        - 创建{：,}，键值对
        - 键值索引，dictname.get(key)或dictname[key]
        - dictname.keys(), dictname.values()-返回包含所有键/值的列表
        - dictname.items()，返回列表，元素是键值对元组

26. hasattr() getattr() setattr() 
    - hasattr(object,name)函数：判断一个对象里面是否有name属性或者name方法，返回bool值，有name属性（方法）返回True，否则返回False
    - getattr(object, name[,default])函数：获取对象object的属性或者方法，如果存在则打印出来，如果不存在，打印默认值，默认值可选。注意：如果返回的是对象的方法，则打印结果是：方法的内存地址，如果需要运行这个方法，可以在后面添加括号().
    - setattr(object, name, values)函数：给对象的属性赋值，若属性不存在，先创建再赋值




















