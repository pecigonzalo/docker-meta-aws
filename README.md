docker run \
  --log-driver=json-file \
  --name=meta-aws \
  --restart=always \
  -d \
  -p $LOCAL_IP:9024:5000 \
  -e AWS_REGION=$AWS_REGION \
  -e MANAGER_SECURITY_GROUP_ID=$MANAGER_SECURITY_GROUP_ID \
  -e WORKER_SECURITY_GROUP_ID=$WORKER_SECURITY_GROUP_ID \
  -v /var/run/docker.sock:/var/run/docker.sock \
  pecigonzalo/docker-meta-aws
