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
# Author: Dmitry Monakhov <dmonakhov@gmail.com>
#

import os

from avocado import Test
from avocado import main
from avocado.utils import archive
from avocado.utils import process
from avocado.utils.software_manager import SoftwareManager


class PostTest(Test):

    """
    Portmark. This is a test of NetApp's PostMark benchmark designed to simulate
    small-file testing similar to the tasks endured by web and mail servers.
    This test profile will set PostMark to perform 25,000 transactions with 500
    files simultaneously with the file sizes ranging between 5 and 512 kilobytes
    :see: https://openbenchmarking.org/test/pts/postmark
    """

    def setUp(self):
        """
        Build 'postmark'.
        """
        sm = SoftwareManager()
        if not sm.check_installed("gcc") and not sm.install("gcc"):
            self.error("Gcc is needed for the test to be run")

        locations = ['ftp://ftp.uk.debian.org/debian/pool/main/p/postmark/postmark_1.51.orig.tar.gz',
                     'http://ftp.gva.es/mirror/debian/pool/main/p/postmark/postmark_1.51.orig.tar.gz',
                     'ftp://ftp.nz.freebsd.org/pub/debian-amd64/debian-amd64/pool/main/p/postmark/postmark_1.51.orig.tar.gz']
        tarball = self.fetch_asset('postmark-1.51.tar.gz', locations=locations,
                                   algorithm='sha1',
                                   asset_hash='2cf0be75e3cb255f36fb1f3e412bcf8f81b39969')
        archive.extract(tarball, self.srcdir)
        postmark_version = os.path.basename(tarball.split('.tar.')[0])
        self.log.info("postmark_version %s" % postmark_version)
        process.run('ls -lh %s' % self.srcdir)
        self.srcdir = os.path.join(self.srcdir, postmark_version)
        os.chdir(self.srcdir)
        process.run('cc -O3 postmark-1.51.c -o postmark')

    def test(self):
        """
        Execute 'postmark' with appropriate parameters.
        """
        config = self.params.get('config', default='files1k_trans1k.pmrc')
        cmd = '%s/postmark %s' % (self.srcdir,
                                  os.path.join(self.datadir, config))
        process.system(cmd)


if __name__ == "__main__":
    main()
