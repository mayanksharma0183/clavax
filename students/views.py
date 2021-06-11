from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from students.models import ClassesModel,StudentDetails,TokenModel
from students.serializer import ClassNameSerializers,StudentRegisterSerializer,StudentLoginSerializer
from rest_framework.response import Response
import time
from datetime import datetime
# Create your views here.




class ClassNameView(APIView):

    def post(self,request):
        response = {"error":"","data":""}
        data = request.data
        try:
            if 'class_name' not in data:
                raise Exception("Please Provide 'class_name' ")
            data['slug'] = data['class_name'].lower()
            serializer_class = ClassNameSerializers(data=data)
            if serializer_class.is_valid():
                serializer_class.save()
                response['data']=serializer_class.data
        except Exception as e:
            print(e)
            response['error']=e.__str__()
        return Response(response)

    def get(self,request):
        response = {"error": "", "data": ""}
        try:
            queryset = ClassesModel.objects.all()
            serializer_class = ClassNameSerializers(queryset,many=True)
            response['data']=serializer_class.data
        except Exception as e:
            response['error']=e.__str__()
        return Response(response)



class StudentRegisterView(APIView):

    def post(self,request):
        response = {"error": "", "data": ""}
        try:
            data = request.data
            print(data)
            validate_fields = ['first_name','last_name','email','password','date_of_birth','class_name','student_image']
            for i in validate_fields:
                if i not in data or data[i] is None:
                    raise Exception('{0} Field Is Mandatory'.format(i))
            try:
                StudentDetails.objects.get(email=data['email'])
                response['error'] = "Student Is Already Register"
                return Response(response)
            except:
                get_class_obj = ClassesModel.objects.get(slug=data['class_name'])
                data['class_name'] = get_class_obj
                data['date_of_birth'] = time.mktime(datetime.strptime(data['date_of_birth'], "%d/%m/%Y").timetuple())
                serializer_class = StudentRegisterSerializer(data=data)
                if serializer_class.is_valid():
                    serializer_class.save()
                    response['data'] = serializer_class.data
        except Exception as e:
            response['error']=e.__str__()
        return Response(response)


class StudentLoginView(APIView):

    def post(self,request):
        response = {}
        try:
            data = request.data
            serializer_class = StudentLoginSerializer(data=data)
            if serializer_class.is_valid():
                user = serializer_class.user
                if 'token' not in user:
                    raise Exception(user['error'])
                response['token'] = user['token']
        except Exception as e:
            response['error'] = e.__str__()
        return Response(response)




