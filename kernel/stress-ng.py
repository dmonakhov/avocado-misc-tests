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
# Copyright: 2016
# Author: Dmitry Monakhov <dmonakhov@openvz.org>
#

import os

from avocado import Test
from avocado import main
from avocado.utils import archive
from avocado.utils import process
from avocado.utils import build
from avocado.utils.software_manager import SoftwareManager
from avocado.utils import distro


class Smatch(Test):

    '''
    stress-ng http://kernel.ubuntu.com/~cking/stress-ng/

    '''

    def setUp(self):
        '''
        Build smatch
        '''
        src_url = 'http://kernel.ubuntu.com/~cking/tarballs/stress-ng/stress-ng-0.07.13.tar.gz'

        deps = ['make', 'gcc', 'git']
        header_deps = []
        detected_distro = distro.detect()

        if detected_distro.name == "fedora" or detected_distro.name == "redhat":
            deps += ['libaio-devel', 'libattr-devel',
                     'libbsd-devel', 'libcap-devel', 'libgcrypt-devel',
                     'keyutils-libs-devel', 'lksctp-tools-devel', 'zlib-devel']
            
        if detected_distro.name == "Ubuntu" or detected_distro.name == "debian":
            deps += ['libaio-dev', 'libapparmor-dev', 'libattr1-dev',
                     'libbsd-dev', 'libcap-dev', 'libgcrypt11-dev',
                     'libkeyutils-dev', 'libsctp-dev', 'zlib1g-dev']
            
        sm = SoftwareManager()
        for pkg in deps:
            if not sm.check_installed(pkg) and not sm.install(pkg):
                self.error("Package %s is needed for the test to be run" % pkg)

        for header in header_deps:
            if not os.access(header, os.R_OK):
                self.log.debug("%s missing - trying to install", header)
                pkg = sm.provides(header)
                if pkg is None:
                    self.error("Unable to find header %s to satisfy 'smatch' dependence" % header)
                else:
                    sm.install(pkg)

        tarball = self.fetch_asset(src_url)
        archive.extract(tarball, self.srcdir)


        tarball = self.fetch_asset(src_url)
        data_dir = os.path.abspath(self.datadir)
        archive.extract(tarball, self.srcdir)
        version = os.path.basename(tarball.split('.tar.')[0])
        self.srcdir = os.path.join(self.srcdir, version)
        self.log.debug('verions:%s srcdir:%s' % (version, self.srcdir))
        build.make(self.srcdir)

    def test(self):

        os.chdir(self.srcdir)
        process.system('./stress-ng --cpu 0 --cpu-method all --vm 1 --vm-bytes 4G --verify -v --metrics -t 48h')
        #process.system('./stress-ng --all 2')

if __name__ == "__main__":
    main()
