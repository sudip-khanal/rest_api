from django.shortcuts import render
from . models import Student
from . seriliziers import StudentSerilizier
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
# Create your views here.
#viewset based api
class StudentApiViewSet(viewsets.ViewSet):
    def list(self,request):
        stu = Student.objects.all()
        serilizier = StudentSerilizier(stu,many=True)
        return Response (serilizier.data)
    
    def retrive(self,request,pk=None):
        id= pk
        if id is not None:
            stu = Student.objects.get(id)
            serilizier = StudentSerilizier(stu)
            return Response (serilizier.data)

    def create(self,request):
        serilizier = StudentSerilizier(data=request.data)
        if serilizier.is_valid():
            serilizier.save()
            return Response ({'msg':'data creeated'},status=status.HTTP_201_CREATED)
        return Response(serilizier.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def updata(self,request,pk):
        id=pk
        stu = Student.objects.get(pk=id)
        serilizier = StudentSerilizier(stu,data=request.data)
        if serilizier.is_valid():
            serilizier.save()
            return Response ({'msg':'data updatae'},status=status.HTTP_200_OK)
        return Response(serilizier.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def destoy(self,request,pk):
        id=pk
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response ({'msg':'data deleted'},status=status.HTTP_200_OK)


