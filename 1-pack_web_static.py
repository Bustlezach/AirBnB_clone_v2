from fabric.api import local
from datetime import datetime

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

