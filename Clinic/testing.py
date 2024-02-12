import requests
from multiprocessing import Pool
from faker import Faker
import random

faker = Faker()


def make_request(api_url, headers):
    response = requests.get(api_url, headers=headers)
    print(f'response from {headers["Tenant-id"]}: {response.text}')

def make_put_request(api_update_url, headers):
    random_data = {
    'doctor_name': str(faker.name()),
    'patient_name': str(faker.name())
    }

    response = requests.put(api_update_url, data=random_data, headers=headers)
    print(f'response from {headers["Tenant-id"]}: {response.text}')

api_url = 'http://127.0.0.1:8000/get-api/'
api_update_url = 'http://127.0.0.1:8000/edit-api/'

headers_list = [
    {'Tenant-id': 'tenant1'},
    {'Tenant-id': 'tenant2'},
    {'Tenant-id': 'tenant1'},
    {'Tenant-id': 'tenant2'},
]
num_workers = 1
while True:
    random.shuffle(headers_list)
    with Pool(num_workers) as pool:
        pool.starmap(make_request, [(api_url, headers) for headers in headers_list])

    print('PUT API')
    with Pool(num_workers) as pool:
        pool.starmap(make_put_request, [(api_update_url, headers) for headers in headers_list])