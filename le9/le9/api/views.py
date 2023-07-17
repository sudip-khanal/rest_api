from django.shortcuts import render

from .models import Student
from .seriliziers import StudentSerilizier
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

#basic Authentication to access the application
class StudentApi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerilizier
    #for localy authentication
    #authentication_classes =[BasicAuthentication]
    #permission_classes =[IsAuthenticated]

# to define globaly we have to write default authentiction in settings file