#!/bin/sh -e

TEST=ext4/024
/devel/xfstests-bld/kvm-xfstests.sh \
    --kernel /d/kernel/linux.git/ \
    -I /d/xfstests-tytso-root_fs.img.x86_64 \
    --update-xfstests-tar \
    -c 4k $TEST $*
