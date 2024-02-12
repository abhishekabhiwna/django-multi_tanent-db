"""
Routing class implements methods but with no args so we can't pass our
tenants db request to it. We need to use middleware to set the db name
"""

from .middleware import get_current_db_name


class ClinicRouter:

    def db_for_read(self, model, **hints):
        return get_current_db_name()

    def db_for_write(self, model, **hints):
        return get_current_db_name()

    def allow_relation(self, *args, **kwargs):
        return True

    def allow_migrate(self, *args, **kwargs):
        return None

    def allow_syncdb(self, *args, **kwargs):
        return None
