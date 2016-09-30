#! /bin/sh -e





setsid bash -c "echo test; sleep 1000 ;echo test" &>/dev/null < /dev/null &
