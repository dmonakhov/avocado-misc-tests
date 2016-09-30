#!/usr/bin/env python

import os

from avocado import Test
from avocado import main
from avocado.utils import kernel


class LinuxBuildTest(Test):

    """
    Execute the Linux Build test.

    :param linux_version: kernel version to be built
    :param linux_config: name of the config file located in deps path
    """

    def setUp(self):
        kernel_version = self.params.get('linux_version', default='4.7')
        linux_config = self.params.get('linux_config', default=None)
        if linux_config is not None:
            linux_config = os.path.join(self.datadir, linux_config)

        #linux_config = '/devel/xfstests-bld.git/kernel-configs/ext4-x86_64-config-4.7'

        linux_config = self.fetch_asset('http://autotest.qa.sw.ru/pub/config-4.5.5-300.fc24.x86_64')
        self.linux_build = kernel.KernelBuild(kernel_version,
                                              linux_config,
                                              self.srcdir,
                                              self.cache_dirs)

        self.linux_build.asset_path = self.fetch_asset("https://cdn.kernel.org/pub/linux/kernel/v4.x/linux-4.7.tar.gz")

        #self.linux_build.download()
        self.linux_build.uncompress()

        #self.linux_build.fetch_git_repo("http://github.com/torvalds/linux")
        self.linux_build.configure()

    def test(self):
        self.linux_build.build()


if __name__ == "__main__":
    main()
