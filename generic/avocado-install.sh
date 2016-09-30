#! /bin/bash
# installer for rhel7
host=$1

if [ -z $host ]; then
    echo "Usage: $0 host"
    exit 1
fi
# Add avocado repository and install avocado
ssh $host "yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm && \
    curl https://repos-avocadoproject.rhcloud.com/static/avocado-el.repo -o /etc/yum.repos.d/avocado.repo &&
    yum install -y avocado avocado-plugins-output-html"
