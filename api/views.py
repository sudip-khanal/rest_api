import io
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from . models import Student
from .seriliziers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def Student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serilizier = StudentSerializer(stu)
            json_data = JSONRenderer().render(serilizier.data)
            return HttpResponse(json_data,content_type='application/json')
        stu = Student.objects.all()
        serilizier = StudentSerializer(stu,many=True)
        json_data = JSONRenderer().render(serilizier.data)
        return HttpResponse(json_data,content_type='application/json')
    if request.method == 'POST':   
        json_data = request.body
        stream = io.BytesIO(json_data) 
        pythondata = JSONParser().parse(stream)
        serilizier = StudentSerializer(data=pythondata)
        if serilizier.is_valid():
            serilizier.save()
            res = {'msg':'Data is Inserted'}
            json_data = JSONRenderer().render(res)
            return HttpResponse (json_data,content_type='application/json')
        json_data = JSONRenderer().render(serilizier.errors)
        return HttpResponse (json_data,content_type='application/json')
    
    if request.method == 'PUT': 
        json_data = request.body
        stream = io.BytesIO(json_data) 
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        #complete update required all data from user/client 
        #serilizier = StudentSerializer(stu,data=pythondata)

        # for partial update-all data are not required
        serilizier = StudentSerializer(stu,data=pythondata,partial=True)
        if serilizier.is_valid():
            serilizier.save()
            res={'msg':'data updated successfully'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serilizier.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method == 'DELETE': 
        json_data = request.body
        stream = io.BytesIO(json_data) 
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res ={'msg':'Data Deleted Successfully'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type='application/json')
        return JsonResponse(res,safe=False)
    









