#!/bin/sh -e

TEST="ext4/023 ext4/024 ext4/301 ext4/302 ext4/303 ext4/304"
/devel/xfstests-bld/kvm-xfstests.sh \
    --kernel /d/kernel/linux.git/ \
    -c 4k $TEST
