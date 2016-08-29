controller:
  image: registry.cn-hangzhou.aliyuncs.com/denverdino/docker-serverless-controller
  environment:
    - CLUSTER_URL=${CLUSTER_URL}
  labels:
    aliyun.addon: "serverless"
    aliyun.routing.port_5000: serverless