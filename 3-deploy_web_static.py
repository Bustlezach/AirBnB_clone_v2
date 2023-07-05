#!/usr/bin/python3
"""Full deployment"""
from fabric.api import *
import os.path
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['18.206.207.78', '100.25.14.62']


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    t = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(t.year,
                                                         t.month,
                                                         t.day,
                                                         t.hour,
                                                         t.minute,
                                                         t.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file


def do_deploy(archive_path):
    """Deploy the tgz file package.

    Args:
        archive_path (str): The path of the archive to distribute.
    Returns:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    f_name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".format(f_name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".format(f_name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file, f_name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(f_name, f_name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".format(f_name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(f_name)).failed is True:
        return False
    return True


def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)

