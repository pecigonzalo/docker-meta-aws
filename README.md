# Docker Swarm for AWS Metadata Service
Provides cluster metadata and serves tokens

*Example project:* **[Terraform docker-swarm](https://github.com/pecigonzalo/tf-docker-swarm)**

### Description
This container will provide general cluster metadata to the rest of the swarm cluster, in it current
state it just provides tokens for Swarm members to join a Swarm cluster.

### Usage
##### Paramaters
| Parameter | Example | Description |
|-----------|:-------:|:------------|
| AWS_REGION | eu-central-1 | AWS Region ID |
| MANAGER_SECURITY_GROUP_ID | sg-asdasdasd | Security group to allow Manager members from |
| WORKER_SECURITY_GROUP_ID | sg-asdasdasd | Security group to allow Worker members from |

##### Example
```
docker run -d \
  --name=meta-aws \
  --restart=always \
  -p $LOCAL_IP:9024:5000 \
  -e AWS_REGION=$AWS_REGION \
  -e MANAGER_SECURITY_GROUP_ID=$MANAGER_SECURITY_GROUP_ID \
  -e WORKER_SECURITY_GROUP_ID=$WORKER_SECURITY_GROUP_ID \
  -v /var/run/docker.sock:/var/run/docker.sock \
  pecigonzalo/docker-meta-aws
```
