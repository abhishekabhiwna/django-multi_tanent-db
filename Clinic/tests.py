import requests
from django.test import TestCase
from Clinic.models import Doctor
from faker import Faker
import random
from concurrent.futures import ThreadPoolExecutor


# Create your tests here.


class DoctorModelTest(TestCase):
    doctor_name = 'Dr. Smith 2'

    db_names = ['default', 'db2', 'db3']

    payload = {}
    headers = {}

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        return Doctor.objects.create(doctor_name=cls.doctor_name,
                                     patient_name='John Doe 2')

    def test_doctor_creation(self):
        w = self.setUpTestData()
        self.assertTrue(isinstance(w, Doctor))
        self.assertEqual(self.doctor_name, w.doctor_name)

    def test_doctor_name_label(self):
        doctor = Doctor.objects.get(id=1)
        field_label = doctor._meta.get_field('doctor_name').verbose_name
        self.assertEquals(field_label, 'doctor name')

    def test_patient_name_label(self):
        doctor = Doctor.objects.get(id=1)
        field_label = doctor._meta.get_field('patient_name').verbose_name
        self.assertEquals(field_label, 'patient name')

    def create_doctor_objects(self):
        # Create a Faker instance for generating fake names
        faker = Faker()

        # Randomly select a database name
        selected_db = random.choice(self.db_names)

        # Generate fake names
        doctor_name = faker.name()
        patient_name = faker.name()
        print(selected_db, doctor_name, patient_name)
        # Create Doctor object using the selected database
        Doctor.objects.using(selected_db).create(
            doctor_name=doctor_name,
            patient_name=patient_name
        )

    def test_pool_code(self):
        # Number of objects to create
        num_objects = 5  # Change this to the desired number of objects to
        # create
        # Create a ThreadPoolExecutor with a maximum of 5 threads
        with ThreadPoolExecutor(max_workers=5) as executor:
            # Submit tasks to the executor Each task will execute the
            # create_doctor function and return a Future object representing
            # the result of the execution
            futures = [executor.submit(self.create_doctor_objects) for _ in
                       range(num_objects)]

            # Wait for all tasks to complete
            for future in futures:
                future.result()

        print("All Doctor objects created successfully.")

    def test_tenant_get(self):
        url = "http://clinic1.localhost:8000/"

        response = requests.request("GET", url,
                                    headers=self.headers, data=self.payload)

        print(response.text)

    def test_tenant_post(self):
        pass
