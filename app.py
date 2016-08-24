from flask import Flask
from redis import Redis
import os
import docker

app = Flask(__name__)
#redis = Redis(host='redis', port=6379)
docker_client = None

def get_docker_client():  
    tls_config = docker.tls.TLSConfig(
        client_cert=('/etc/docker/service.pem', '/etc/docker/service-key.pem'),
        verify='/etc/docker/acs-ca.pem'
    )
    cluster_url = os.environ.get('CLUSTER_URL')
    return docker.Client(base_url=cluster_url, tls=tls_config)

@app.route('/')
def hello():
    #redis.incr('hits')
    container = docker_client.create_container('busybox')
    docker_client.start(container)
    return 'Hello World from container %s!' % container


if __name__ == "__main__":
    docker_client = get_docker_client()
    app.run(host="0.0.0.0", debug=True)
