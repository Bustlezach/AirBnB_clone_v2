#!/usr/bin/python3
"""Compress before sending"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """Generates a .tgz archive"""
    # Create version directory
    local("mkdir -p versions")

    # Create the file name using the current date and time
    t = datetime.now()
    file_name = f"web_static_{t.year}{t.month}{t.day}{t.hour}{t.minute}{t.second}.tgz"

    # Compress the files into a tar archive
    file_store = local(f"tar -cvzf versions/{file_name}")
    
    if file_store.succeeded:
        return 'versions/{}'.format(file_name)
    else:
        return None
    
