from dotenv import load_dotenv
import configparser

load_dotenv()

config = configparser.ConfigParser()
config.read('config.ini')

# These 3 functions will be called when the request will come for Admin panel
def hostname_from_request(request):
    """
    Take the request, remove the port and return bare url.
    """
    return request.get_host().split(':')[0].lower()


def tenant_db_from_request_for_admin(request):
    """
    call other two functions, compare host url and dictionary and return db name for tenant
    """
    host_name = hostname_from_request(request)
    tenant_map = get_tenants_map()
    db =tenant_map.get(host_name)
    return db


def get_tenants_map():
    """
    return a dictionary of tenant urls and db names
    """
    return {
        'clinic1.localhost': 'default',
        'clinic2.localhost': 'db2'
    }


# These 2 functions will be called when the request will come for normal APIs 
def tenant_db_from_request(request):
    """
    Extract tenant ID from headers, compare host URL with dictionary, and return the database name for the tenant.
    """
    tenant_id = request.headers.get('Tenant-id')
    if tenant_id:
        db = get_database_uri(tenant_id)
    else:
        db = 'default'
    return db


def get_database_uri(tenant_id):
    return config.get('tenants', tenant_id)