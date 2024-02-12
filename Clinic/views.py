from rest_framework.views import APIView
from .models import Doctor
from .serializers import DoctorSerializer
from rest_framework.response import Response
from rest_framework import status
from copy import deepcopy

class GetDoctorView(APIView):
    def get(self, request):
        data = Doctor.objects.all()
        serializer = DoctorSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddTenantNameView(APIView):
    def put(self, request):
        data = deepcopy(request.data)

        tenant_id = request.headers.get('tenant_id')
        d_name = data.get('doctor_name').split()
        d_name[1] = tenant_id
        d_name = ' '.join(d_name)
        data.update({'doctor_name': d_name})

        random_data = Doctor.objects.order_by('?').first()
        # updated_data = {'doctor_name': f'{tenant_id}_{data.doctor_name}'}
        serializer = DoctorSerializer(instance=random_data, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)