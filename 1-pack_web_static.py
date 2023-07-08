#!/usr/bin/env bash
"""Make achive file"""

from fabric.api import local
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['52.205.172.113', '54.160.64.104']

def do_pack():
    """Generate a .tgz archive"""

    # Generate the archive path
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        archive_path = "versions/web_static_{}.tgz".format(now)
        result = local("tar -cvzf {} web_static".format(archive_path))
        return archive_path

    except Exception as e:
        return None

