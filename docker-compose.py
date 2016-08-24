controller:
  image: registry.cn-hangzhou.aliyuncs.com/denverdino/docker-serverless-sample
  environment:
    - CLUSTER_URL=${CLUSTER_URL}
  labels:
    aliyun.addon: "dns"
    aliyun.routing.port_5000: serverless
