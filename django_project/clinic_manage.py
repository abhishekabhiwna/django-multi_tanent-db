"""
To start working we need to create superuser for each db and perform migrations.
This won't work for all dbs, we need to specify db name in command. So we need to override this as well
"""

import os
import sys

from Clinic.middleware import set_db_for_router

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # set db name for router

    from django.db import connection

    args = sys.argv
    db = args[1]
    with connection.cursor() as cursor:
        set_db_for_router(db)
        del args[1]
        execute_from_command_line(args)
