#! /bin/sh -e

docker build --force-rm -t debian-avocado -f contrib/docker/Dockerfile.debian \
    https://github.com/dmonakhov/avocado.git#inst

docker tag debian-avocado alice.qa.sw.ru:5000/debian-avocado
docker push alice.qa.sw.ru:5000/debian-avocado
ansible avocado -a 'docker pull alice.qa.sw.ru:5000/debian-avocado'

# This is cleanup stage it should not affect whole deployment
docker rmi debian-avocado
ansible avocado -m shell -a 'docker  rmi $(docker images -f "dangling=true" alice.qa.sw.ru:5000/debian-avocado -q)' || \
    /bin/true
