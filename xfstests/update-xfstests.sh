#!/bin/sh -e


TEST=ext4/024
cd /devel/xfstests-bld/xfstests-dev
git remote add LOCAL /d/xfstests.git
git fetch LOCAL
git reset --hard LOCAL/guilt/dev1
git remote remove LOCAL

cd /devel/xfstests-bld/fio
git remote add LOCAL /d/tools/fio.git
git fetch LOCAL
git reset --hard LOCAL/guilt/master
git remote remove LOCAL

cd ../
./build-all --xfstests-only
./build-all --fio-only

./gen-tarball
cd /devel/xfstests-bld/kvm-xfstests/test-appliance
cp /d/xfstests-dmonakhov-root_fs.img.x86_64 root_fs.img
./gen-image --update
