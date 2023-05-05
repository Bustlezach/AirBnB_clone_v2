#!/usr/bin/python3
"""Deploy archive!"""
from fabric.api import *
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['18.206.207.78', '100.25.14.62']


def do_pack():
    """the project directory to unpack .tgz"""
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    local('sudo mkdir -p ./versions')
    path = './versions/web_static_{}'.format(now)
    local('sudo tar -czvf {}.tgz web_static'.format(path))
    name = '{}.tgz'.format(path)
    if name:
        return name
    else:
        return None


def do_deploy(archive_path):
    """Deploy the tgz file package"""
    try:
        file_name = archive_path.split('/')[-1]
        path = '/data/web_static/releases/' + file_name.strip('.tgz')
        cur = '/data/web_static/current'
        put(archive_path, '/tmp')
        run('mkdir -p {}/'.format(path))
        run('tar -xzf /tmp/{} -C {}'.format(file_name, path))
        run('rm /tmp/{}'.format(file_name))
        run('mv {}/web_static/* {}'.format(path, path))
        run('rm -rf {}/web_static'.format(path))
        run('rm -rf {}'.format(cur))
        run('ln -s {} {}'.format(path, cur))
        print('New version deployed!')
        return True
    except ValueError:
        return False
    
