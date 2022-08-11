# pip

1. pip install package, no module named xxx
    - pip需要更新
        - pip install --upgrade 升级包名
        - pip install --upgrade/-U pip
        - python -m pip install --upgrade pip
    - 包名错误，类似cv2 == opencv-python  yaml==PyYAML

2. apt update / upgrade
    - apt update : 同步最新包的版本，不对包进行升级
    - apt upgrade (包名): 升级包，不加包名升级所有包