#!/usr/bin/python3
"""Compress before sending"""
from fabric.api import *
from datetime import datetime
import os.path


def do_pack():
    """Generates a .tgz archive"""
   
   
    # Create the file name using the current date and time
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
    