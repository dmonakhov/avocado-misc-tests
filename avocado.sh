#! /bin/bash

ssh yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
# Add avocado repository and install avocado
curl https://repos-avocadoproject.rhcloud.com/static/avocado-el.repo -o /etc/yum.repos.d/avocado.repo
yum install -y avocado avocado-plugins-output-html
