#基于的基础镜像
FROM python:3.7

#工作目录
WORKDIR /usr/src/app

#复制requirements.txt文件
COPY requirements.txt ./

#安装依赖包
RUN pip install -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com  --no-cache-dir -r requirements.txt

# 安装支持
#RUN pip install -r requirements.txt
COPY /QQbot ./QQbot
#COPY /Pipfile /Pipfile
#COPY /Pipfile.lock /Pipfile.lock

#暴露 8080端口，监听服务器
EXPOSE 8080

# 设置工作目录
CMD ["python", "./QQbot/bot.py"]