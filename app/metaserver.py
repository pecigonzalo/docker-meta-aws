import os

import boto3
import docker
from flask import abort
from flask import Flask
from flask import request


AWS_REGION = os.environ['AWS_REGION']
MANAGER_SG_ID = os.environ['MANAGER_SECURITY_GROUP_ID']
WORKER_SG_ID = os.environ['WORKER_SECURITY_GROUP_ID']

docker_client = docker.from_env()
aws_client = boto3.client('ec2', region_name=AWS_REGION)
boto3.client('ecs')
app = Flask(__name__)


def get_instance(ip_address):
    response = aws_client.describe_instances(
        Filters=[
            {
                'Name': 'network-interface.addresses.private-ip-address',
                'Values': [ip_address]
            }
        ]
    )

    return response['Reservations'][0]['Instances'][0]


def get_manager_token():
    try:
        token = str(docker_client.swarm.attrs['JoinTokens']['Manager'])
    except Exception:
        token = ''

    return token


def get_worker_token():
    try:
        token = str(docker_client.swarm.attrs['JoinTokens']['Worker'])
    except Exception:
        token = ''

    return token


def check_sg_exist(list, group):
    for sg in list:
        if sg['GroupId'] == group:
            return True
    return False


@app.route('/token/manager/')
def return_manger_token():
    instance = get_instance(request.remote_addr)
    print('Source IP: {}'.format(request.remote_addr))

    if check_sg_exist(instance['SecurityGroups'], MANAGER_SG_ID):
        return get_manager_token()
    abort(403)


@app.route('/token/worker/')
def return_worker_token():
    instance = get_instance(request.remote_addr)
    print('Source IP: {}'.format(request.remote_addr))

    if check_sg_exist(instance['SecurityGroups'], WORKER_SG_ID):
        return get_worker_token()
    abort(403)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
