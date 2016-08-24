FROM registry.cn-hangzhou.aliyuncs.com/acs/python:3.6
EXPOSE 5000
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python app.py
