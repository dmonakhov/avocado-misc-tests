#!/bin/sh -e

/devel/xfstests-bld/kvm-xfstests.sh \
    --kernel /d/kernel/linux.git/ \
    --update-xfstests-tar \
    -c 4k $@
