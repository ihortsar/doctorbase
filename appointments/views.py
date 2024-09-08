from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class Appointments(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user = request.user
        
        if hasattr(user, 'doctor'):
            doctor = user.doctor
            appointments = Appointment.objects.filter(doctor=doctor)
        elif hasattr(user, 'patient'):
            patient = user.patient
            appointments = Appointment.objects.filter(patient=patient)
        else:
            return Response({"detail": "Unauthorized"}, status=status.HTTP_403_FORBIDDEN)

        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request, *args, **kwargs):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Appointment created successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
