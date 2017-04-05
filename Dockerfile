FROM debian:8
MAINTAINER Gonzalo Peci <pecigonzalo@outlook.com>
ENV DEBIAN_FRONTEND noninteractive

ENV AWS_REGION ''
ENV MANAGER_SECURITY_GROUP_ID ''
ENV WORKER_SECURITY_GROUP_ID ''

EXPOSE 5000

RUN apt-get update && \
  apt-get install -y \
    jq \
    libltdl-dev \
    python-pip \
    wget && \
  pip install -U pip && \
  pip install awscli

COPY ./app /app
WORKDIR /app

RUN pip install -r requirements.txt

COPY entry.sh /

CMD ["/entry.sh"]
