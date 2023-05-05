#!/usr/bin/python3
"""Compress before sending"""
from fabric.api import *
from datetime import datetime
import os.path


def do_pack():
    """Generates a .tgz archive"""
   
   
    # Create the file name using the current date and time
    t = datetime.now()
    file_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(t.year,
                                                         t.month,
                                                         t.day,
                                                         t.hour,
                                                         t.minute,
                                                         t.second)

   
	

	# Create version directory
	if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
			
	# Compress the files into a tar archive
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
    
