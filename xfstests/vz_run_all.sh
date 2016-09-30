#!/bin/sh -e


/devel/xfstests-bld/kvm-xfstests.sh \
    --kernel /d/kernel/vz/vzkernel.git/Bld \
    -c 4k -g auto
