from django.shortcuts import render

from .models import Student
from .seriliziers import StudentSerilizier
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

class StudentApi(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerilizier
    #for localy authentication
    # authentication_classes =[BasicAuthentication]
    # permission_classes =[MyPermission]