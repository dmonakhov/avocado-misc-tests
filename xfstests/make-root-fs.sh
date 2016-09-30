#!/bin/sh -e

apt-get update -y
apt-get install -y  debootstrap

MIRROR=https://mirror.yandex.ru/debian/
EXTRA_PKG="emacs-nox strace"
cd /devel/xfstests-bld/kvm-xfstests/test-appliance
./gen-image --mirror $MIRROR -a "$EXTRA_PKG"
cp root_fs.img /d/xfstests-dmonakhov-root_fs.img.x86_64 
