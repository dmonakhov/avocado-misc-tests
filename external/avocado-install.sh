#! /bin/sh -e

# installer for rhel7
host=$1

if [ -z $host ]; then
    echo "Usage: $0 host"
    exit 1
fi
# Add avocado repository and install avocado

RHV=`ssh $host " test -f /etc/redhat-release && cat /etc/redhat-release"`

if [ -z $RHV ]; then
    echo "Unknown distro version"
    exit 1
fi

fedora=`echo "$RHV" |grep Fedora`
if [ $? -eq 0 ]; then
    echo "Fedora detected"
    ssh $host "curl https://repos-avocadoproject.rhcloud.com/static/avocado-fedora.repo -o /etc/yum.repos.d/avocado.repo"
    ssh $host "dnf -y update"
    ssh $host "dnf install -y  avocado avocado-plugins-output-html avocado-examples"
    exit $?
fi
ssh $host "yum install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm; \
    curl https://repos-avocadoproject.rhcloud.com/static/avocado-el.repo -o /etc/yum.repos.d/avocado.repo &&
    yum install -y avocado avocado-plugins-output-html"
