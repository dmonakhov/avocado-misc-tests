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
    Smatch -- The Source Matcher, Official repo git://repo.or.cz/smatch.git
    Kernel usage example:
       make C=1 CHECK="/path/to/smatch --full-path -p=kernel" | tee warns.txt
    After the compile finishes logs stored to smatch_log and smatch_error
    #perf key values = [ 'warning', 'error' ]

    '''

    def setUp(self):
        '''
        Build smatch
        '''
        src_url = 'http://repo.or.cz/smatch.git'
        src_commit = '78b2ea6'

        deps = ['make', 'gcc']
        header_deps = ['/usr/include/sqlite3.h',
                       '/usr/include/llvm']
        detected_distro = distro.detect()

        if detected_distro.name == "fedora" or detected_distro.name == "redhat":
            deps += ['gcc-g++', 'zlib-devel', 'sqlite-devel']
        if detected_distro.name == "fedora":
            deps += ['llvm-devel']
        if detected_distro.name == "Ubuntu" or detected_distro.name == "debian":
            deps += ['g++', 'zlib1g-dev', 'llvm-dev', 'libsqlite3-dev', 'libedit-dev']

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

        full_url = src_url + '/snapshot/' + src_commit + '.tar.gz'
        tarball = self.fetch_asset(full_url)
        archive.extract(tarball, self.srcdir)
        srcdir = 'smatch-' + src_commit
        data_dir = os.path.abspath(self.datadir)
        self.srcdir = os.path.join(self.srcdir, srcdir)

        os.chdir(self.srcdir)
        p1 = 'patch -p1 < %s/%s' % (data_dir, 'install-scripts.patch')
        process.run(p1, shell=True)
        build.make(self.srcdir)

    def test_install(self):

        os.chdir(self.srcdir)
        self.log.info("self.srcdir: %s" % self.srcdir)
        process.run('PREFIX=/usr make install', shell=True)

if __name__ == "__main__":
    main()
