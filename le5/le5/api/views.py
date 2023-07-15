from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . models import Student
from .seriliziers import StudentSerilizier
from rest_framework import status
# Create your views here.
#function based Api View

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def StudentApi(request,pk=None):
    if request.method == 'GET':
        id = pk
        if id is not None:
            stu= Student.objects.get(id=id)
            serilizier = StudentSerilizier(stu)
            return Response(serilizier.data)
        
        stu= Student.objects.all()
        serilizier = StudentSerilizier(stu,many =True)
        return Response(serilizier.data)
    
    if request.method == 'POST':
        serilizier = StudentSerilizier(data=request.data)
        if serilizier.is_valid():
            serilizier.save()
            return Response({'msg':'Data Inerted'},status=status.HTTP_201_CREATED)
        return Response(serilizier.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PUT':
        id = pk
        stu= Student.objects.get(pk=id)
        serilizier = StudentSerilizier(stu,data=request.data)
        if serilizier.is_valid():
            serilizier.save()
            return Response({'msg':'Complete Data Updated'},status=status.HTTP_200_OK)
        return Response(serilizier.errors,status=status.HTTP_400_BAD_REQUEST)
        
    if request.method == 'PATCH':
        id = pk
        stu= Student.objects.get(pk=id)
        serilizier = StudentSerilizier(stu,data=request.data,partial=True)
        if serilizier.is_valid():
            serilizier.save()
            return Response({'msg':'Partial Data Updated'},status=status.HTTP_200_OK)
        return Response(serilizier.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        stu= Student.objects.get(pk=pk)
        stu.delete()
        return Response({'msg':'Data Deleted'},status=status.HTTP_200_OK)
