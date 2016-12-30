#!/bin/sh -ex

cd /devel/xfstests-bld/kvm-xfstests
#/d/xfstests-dmonakhov-root_fs.img.x86_64.dev

./kvm-xfstests \
    --kernel $KERNEL \
    -I $XFSTESTS_IMG \
    $XFSTESTS_FS_CONFIG \
    $XFSTESTS_TESTS

mkdir results
mount disks/vdg results  -oloop
cp -r results $AVOCADO_TEST_OUTPUTDIR
cp -r logs $AVOCADO_TEST_OUTPUTDIR
umount results
rm -rf results logs/*
status=0
./get-results -F $AVOCADO_TEST_OUTPUTDIR/logs/* |  grep Failures && status=1
exit $status

