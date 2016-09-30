#! /bin/sh -e

setsid bash -c "~/kexec-reboot/kreboot -w 100 0" &>/dev/null < /dev/null &
