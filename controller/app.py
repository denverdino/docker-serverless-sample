from flask import Flask
import os
import docker
import time
import acs

app = Flask(__name__)
docker_client = None
acs_client = None

def init_clients():  
    tls_config = docker.tls.TLSConfig(
        client_cert=('/etc/docker/service.pem', '/etc/docker/service-key.pem'),
        verify='/etc/docker/acs-ca.pem'
    )
    cluster_url = os.environ.get('CLUSTER_URL')
    docker_client = docker.Client(base_url=cluster_url, tls=tls_config)
    acs_client = acs.AliyunContainerServiceClient(base_url=cluster_url, tls=tls_config)


@app.route('/test1')
def hello_from_docker():
    container = docker_client.create_container('busybox')
    docker_client.start(container)
    return 'Hello World from container %s!' % container


test_template = '''
version: "2"
labels:
  aliyun.project_type: "batch"
services:
  test:
    image: registry.cn-hangzhou.aliyuncs.com/denverdino/docker-serverless-sample
    restart: no
    cpu_shares:  10
    mem_limit: 100000000
    labels:
      aliyun.addon: "serverless"
      aliyun.scale: "10"
      aliyun.retry_count: "20"
      aliyun.remove_containers: "remove-all"
'''

@app.route('/test2')
def hello_from_aliyun():
    project_name="hello%d" % time.time()
    acs_client.create_project(project_name, template=test_template)
    return 'Hello World from Aliyun %s!' % project_name


if __name__ == '__main__':
    init_clients()
    app.run(host="0.0.0.0", debug=True)
