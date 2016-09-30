#!/bin/sh -e


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
./build-all
curl autotest.qa.sw.ru/pub/perf.tar.xz | tar Jx -C bld/sbin/

./gen-tarball
cd /devel/xfstests-bld/kvm-xfstests/test-appliance
cp /d/xfstests-dmonakhov-root_fs.img.x86_64 root_fs.img
./gen-image --update
cp root_fs.img /d/xfstests-dmonakhov-root_fs.img.x86_64.dev
