from django.shortcuts import render

# Create your views here.
from . models import Student
from . seriliziers import StudentSerilizier
from rest_framework import viewsets

# ModelViewsets

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerilizier

# Read Only Viewset
class StudentReadOnlyViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerilizier
