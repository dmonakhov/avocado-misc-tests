#!/bin/sh -ex

cd /devel/xfstests-bld/kvm-xfstests
#/d/xfstests-dmonakhov-root_fs.img.x86_64.dev

./kvm-xfstests \
    --kernel $KERNEL \
    -I $XFSTESTS_IMG \
    $XFSTESTS_FS_CONFIG \
    $XFSTESTS_TESTS

cp logs $AVOCADO_TEST_OUTPUTDIR
