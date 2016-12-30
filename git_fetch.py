#!/usr/bin/env python


import os
from avocado import Test
from avocado import main
from avocado.utils import git


class GitTest(Test):

    def test_fetch_local(self):
        linux_dir = os.path.join(self.srcdir, "linux.git")
        git.get_repo("https://github.com/torvalds/linux.git",
                     base_uri="/devel/kernel/linux.git/",
                     destination_dir=linux_dir)

    def test_fetch_rsync(self):
        linux_dir = os.path.join(self.srcdir, "linux.git")
        git.get_repo("https://github.com/torvalds/linux.git",
                     base_uri="rsync://bob.qa.sw.ru:/devel/kernel/linux.git/.git",
                     destination_dir=linux_dir)

    def test_fetch_mirror_rsync(self):
        linux_dir = os.path.join(self.srcdir, "linux.git")
        git.get_repo("https://github.com/torvalds/linux.git",
                     base_uri="rsync://autotest.qa.sw.ru:/git-mirror/kernel/linux.git",
                     destination_dir=linux_dir)


#    def test_fetch_ssh(self):
#        linux_dir = os.path.join(self.srcdir, "linux.git")
#        git.get_repo("https://github.com/torvalds/linux.git",
#                     base_uri="ssh://bob.qa.sw.ru:/devel/kernel/linux.git",
#                     destination_dir=linux_dir)
#
#    def test_fetch_github(self):
#        linux_dir = os.path.join(self.srcdir, "linux.git")
#        git.get_repo("https://github.com/torvalds/linux.git",
#                     destination_dir=linux_dir)
#
if __name__ == "__main__":
    main()
