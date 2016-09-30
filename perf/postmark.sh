#! /bin/sh -e

rm -rf   /root/tests/host_32_ve_1_client_1
mkdir -p /root/tests/host_32_ve_1_client_1/test_1
echo -e 'set location /root/tests/host_32_ve_1_client_1/test_1\nset number 3000000\nset transactions 1000000\nrun' \
    | /sdb/tests/atomic/bin/lin64/postmark
