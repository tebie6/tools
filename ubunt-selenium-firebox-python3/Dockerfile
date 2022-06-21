FROM ubuntu:20.04

# 设置默认时区
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Shanghai

# 更新apt-get包、创建和宿主机映射项目目录
RUN apt-get update && mkdir data

# 安装 firefox、常用命令、图形包用于ORC识别
RUN apt-get install -y firefox vim wget pip libgl1-mesa-glx

# 下载firefox操作驱动geckodriver
RUN cd /usr/local/src \
&& wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz \
&& tar -zxvf geckodriver-v0.30.0-linux64.tar.gz \
&& mv /usr/local/src/geckodriver /usr/local/bin/

# 安装selenium包 和 ddddocr包
RUN pip install selenium -i https://pypi.tuna.tsinghua.edu.cn/simple && pip install ddddocr -i https://pypi.tuna.tsinghua.edu.cn/simple && apt-get clean

# 操作流程
# docker build --no-cache -t ubunt_firebox_selenium_python3 .
# docker run -dit -v /Users/liumingyu/project/tjprotnet_login:/data --name test_demo ubunt_firebox_selenium_python3
# docker exec -it test_demo /bin/bash
# docker exec -it test_demo /bin/bash -c 'python3 /data/main_test.py'



