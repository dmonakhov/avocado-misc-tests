#! /bin/sh -e

cd /d/kernel/linux.git/tools/perf
export LDFLAGS=-static
make clean
make 
