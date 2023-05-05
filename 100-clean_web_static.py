#!/usr/bin/python3
"""Deploy web_static to web servers"""
from fabric.api import *
import os

env.user = 'ubuntu'
env.hosts = ['18.206.207.78', '100.25.14.62']


def do_clean(number=0):
    """Delete out-of-date archives.

        Args:
            number (int): The number of archives to keep.

        If number is 0 or 1, keeps only the most recent archive. If
        number is 2, keeps the most and second-most recent archives,
        etc.
    """
    num = 1 if int(number) == 0 else int(number)
    f_archive = sorted(os.listdir("versions"), reverse=True)
    archive_s = []
    i = 0
    while i < num:
        archive_s.append(f_archive[i])
        i += 1

    with lcd("versions"):
        for ind in f_archive:
            if ind not in archive_s:
                local("rm {}".format(ind))

    with cd("/data/web_static/releases"):
        f_archive = run("ls -tr").split()
        f_archive = [a for a in f_archive if "web_static_" in a]
        [f_archive.pop() for i in range(num)]
        [run("rm -rf {}".format(a)) for a in f_archive]


def deploy():
    """Distributes archive to web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    res = do_deploy(archive_path)
    if not res:
        return False
    res = do_clean(2)
    return res

