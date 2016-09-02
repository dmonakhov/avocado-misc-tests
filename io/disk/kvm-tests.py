#!/usr/bin/env python

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See LICENSE for more details.
#
# Copyright: 2016 Virtuozzo, Inc.
# Author: Dmitry Monakhov
#

import os

from avocado import Test
from avocado import main
from avocado.utils import archive
from avocado.utils import build
from avocado.utils import process


class KVMXfstests(Test):

    """
    """

    def setUp(self):
        """
        Build 'fio'.
        """
        self.xfsdir = '/devel/xfstests-bld'
        self.kernel = self.fetch_asset('http://bob.qa.sw.ru/pub/bzImage-715dca9a4')
        self.root_fs =  self.fetch_asset('http://bob.qa.sw.ru/pub/root_fs.img')
        self.config = self.fetch_asset('http://bob.qa.sw.ru/pub/config.custom')
        process.system("cp %s %s/config.custom" % (self.config, self.xfsdir))
        self.bdir = os.getcwd()
        os.chdir(self.xfsdir)
        process.system("rm -rf xfstests-dev")
        process.system("./get-all")
        process.system("./build-all --xfstests-only")
        process.system("make tarball")
        os.chdir(os.path.join(self.xfsdir, 'kvm-xfstests/test-appliance'))
        process.system('./gen-image --update')
        process.system('scp root_fs.img bob.qa.sw.ru:/var/www/html/pub/')
        os.chdir(self.bdir)
        
    def test(self):
        """
        Execute 'kvm-xfstests' with appropriate parameters.
        """
        os.chdir(os.path.join(self.xfsdir, 'kvm-xfstests'))
        #cmd = './kvm-xfstests -o debug -I %s --kernel  %s -c 4k ext4/023' %  (self.root_fs, self.kernel)
        cmd = './kvm-xfstests -o debug --kernel %s full -X ext4/022' % self.kernel
        process.system(cmd)


if __name__ == "__main__":
    main()
