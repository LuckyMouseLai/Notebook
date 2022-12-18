## Linux
1. grep
    - Global search REgular expression and Print out the line
    - 支持正则表达式和文本的搜索工具
    - 参数
        - -v：排除匹配结果
        - -i：不区分大小写
        - -n: 显示行号
        - -c: 只统计匹配的行数
        - -o: 只输出匹配的内容
        - -w: 只匹配过滤的单词
        - -E：使用egrep命令
        - --color=auto：颜色标注过滤条件
2. ps
    - 查看进程状态
    - 参数
        - -a: 显示所有进程 
        - -u: 显示用户及进程的详细信息
        - -x: 显示没有控制终端的进程
    example：ps aux | grep python

3. |、||、&、&&
    - &：表示任务在后台执行，终端不显示。例：python train.py &
    - &&: 表示上一条命令执行成功，才执行下一条命令。例：echo '1' && echo '2'
    - |: 表示管道，上一条命令的输出，作为下一条命令的参数。例：ps aux | grep python
    - ||: 表示上一条命令执行失败，才执行下一条命令。例：cat ./a.txt || echo 'wrong file'

4. echo
    - 显示文字
    - 常用参数
        - -n: 输出后不换行
    - 常用操作
        - echo 'this is a md file'
            - 输出
        - echo 'this is a md file' > 文件名
            - 覆盖整个文件
        - echo 'this is a md file' >> 文件名
            - 追加