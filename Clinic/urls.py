from django.urls import path
from .views import GetDoctorView, AddTenantNameView

urlpatterns = [
    path('get-api/', GetDoctorView.as_view(), name='get-api'),
    path('edit-api/', AddTenantNameView.as_view(), name='edit-api'),
]
