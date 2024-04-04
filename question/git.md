### Git
1. fatal: unable to access 'xxx': Could not resolve host: github.com
    - git config --global --add remote.origin.proxy "127.0.0.1:port"
    - 注意：需更改port为使用代理的端口号，查看VPN设置，使用时需打开vpn

2. 修改git源(例如远程修改了仓库名称，本地修改git源同步)
    - git remote set-url origin  https://github.com/LuckyMouseLai/ToyRepo.git