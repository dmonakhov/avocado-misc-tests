#!/bin/bash -e

nohup sleep 1000 &
nohup sleep 1001 &
nohup sleep 1003 &

kill $(jobs -p)

exit 1
