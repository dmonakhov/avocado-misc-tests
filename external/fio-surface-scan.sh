#! /bin/sh -e

DEV=/dev/sdb


FIO_COMMON="\
    --thread=1 \
    --bs=1M \
    --direct=1 \
    --iodepth=16 \
    --ioengine=sync \
    --verify=meta \
    --verify_pattern=0xaa555aa5 \
    --verify_interval=512"

FIO_WRITE="
    --name=write-phase \
    --rw=write \
    --fill_device=1 \
    --do_verify=0 \
    --filename=$DEV"

FIO_VERIFY="\
    --name=verify-phase \
    --stonewall \
    --create_serialize=0 \
    --rw=read \
    --do_verify=1 \
    --filename=$DEV"

fio $FIO_COMMON $FIO_WRITE

fio $FIO_COMMON $FIO_VERIFY
