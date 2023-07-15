
# Create your views here.

# Create your views here.
import io
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from . models import Student
from .seriliziers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

@method_decorator(csrf_exempt, name='dispatch')
class StudentAPI(View):
    def get(self,request ,*args, **kwargs):
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
    def post(self,request,*args, **kwargs):   
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
        
    def put(self,request,*args, **kwargs):   
 
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
        
    def delete(self,request,*args, **kwargs):   
 
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
        









