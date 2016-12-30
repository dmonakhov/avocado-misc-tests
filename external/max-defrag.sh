#!/bin/sh -e

00cleanup
00precr


#echo 1 > /sys/kernel/debug/tracing/events/ploop/add_free_extent/enable
#echo 1 > /sys/kernel/debug/tracing/events/ploop/add_reloc_extent/enable
#echo 1 > /sys/kernel/debug/tracing/events/ploop/wbc_ord/enable
#echo 1 > /sys/kernel/debug/tracing/events/ploop/wbc_swap/enable
#echo 1 > /sys/kernel/debug/tracing/events/ploop/piu_single/enable
#echo 1 > /sys/kernel/debug/tracing/events/ploop/piu_multi/enable
#echo 1 > /sys/kernel/debug/tracing/events/ploop/submit_alloc/enable
#echo 1 > /sys/kernel/debug/tracing/events/ploop/make_request/enable
#echo 1 > /sys/kernel/debug/tracing/events/ploop/bio_fast_map/enable
#
#nohup cat /sys/kernel/debug/tracing/trace_pipe >/vz/pip 2>&1 &

echo 256000 > /sys/kernel/debug/tracing/buffer_size_kb

vzctl start 101
vzctl start 102
vzctl start 103
vzctl start 104
sleep 5
precreate

#/root/bin/fsx-samedir
myfWH
ps -eaf |grep fsx |grep -v grep |grep -v wh |wc -l

#nohup myloop2 &
nohup myloop1H &

#nohup e4defrag2-10x-cont.sh &

for ((i=0;i<1000000;i++)); do
    cat /proc/mounts | grep "/vz/root/10" | gawk '{ print $1 " " $2 }' | xargs -n2  e4defrag2.sh
    #sleep 10
    journalctl -k | grep "EXT4-fs error" || continue
    echo $0: FSERROR detected, break test | tee  > /dev/kmsg
    kill -9 $(jobs -p)
    echo kill PPID $PPID
    pkill -9 fsx-linux
    kill -9 $PPID
    echo kill this-pid $$
    kill -9 $$
    exit 1
done
