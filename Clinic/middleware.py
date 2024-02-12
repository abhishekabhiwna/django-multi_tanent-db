import threading
from .utils import tenant_db_from_request, tenant_db_from_request_for_admin

_thread_locals = threading.local()

class ClinicMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            db = tenant_db_from_request_for_admin(request)
        else:
            db = tenant_db_from_request(request)
        setattr(_thread_locals, 'DB', db)
        response = self.get_response(request)
        return response


# set & get db name for router
def get_current_db_name():
    return getattr(_thread_locals, 'DB', None)


def set_db_for_router(db):
    setattr(_thread_locals, 'DB', db)
