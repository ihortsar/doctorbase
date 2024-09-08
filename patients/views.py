from rest_framework.authtoken.models import Token
from appointments.models import Appointment
from appointments.serializers import AppointmentSerializer
from doctors.models import Doctor
from doctors.serializers import DoctorSerializer
from .models import Patient
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import generics
from .serializers import PatientSerializer
from rest_framework.views import APIView


class SignUp(generics.CreateAPIView):
    serializer_class = PatientSerializer


class Login(ObtainAuthToken):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            return Response({"detail": "Invalid username/password."}, status=status.HTTP_400_BAD_REQUEST)
        
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK)
    
    
class Patients(APIView):
    def get(self, request, *args, **kwargs):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, patient_id, *args, **kwargs):
        try:
            patient = Patient.objects.get(id=patient_id)
            patient.delete()
            return Response(
                {"message": "Patient deleted successfully"},
                status=status.HTTP_204_NO_CONTENT,
            )
        except Patient.DoesNotExist:
            return Response(
                {"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND
            )
