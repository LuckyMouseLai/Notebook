### Git
1. fatal: unable to access 'xxx': Could not resolve host: github.com
    - git config --global --add remote.origin.proxy "127.0.0.1:port"
    - 注意：需更改port为使用代理的端口号，查看VPN设置