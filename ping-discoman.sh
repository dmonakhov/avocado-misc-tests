#!/bin/sh -e

for ((i=0;i<1000;i++)); do
    ansible discoman* -t $AVOCADO_TEST_OUTPUTDIR/out-$i -m setup
    sleep 100
done
