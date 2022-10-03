from ast import Delete
from email import message
from functools import partial
from logging import exception
from urllib import response
from wsgiref.util import request_uri
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken



# Create your views here.


@api_view(['Get'])
def get_book(request):
    book_objs = Book.objects.all()
    serializer = Bookserializers(book_objs, many=True)
    return Response({'status':200, 'payload':serializer.data})



class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializers(data=request.data)
        
        if not  serializer.is_valid():
            return response({'status':403, 'errors': serializer.error, 'message': "invalid "})
        serializer.save()

        user = User.objects.get(username= serializer.data['username'])
        # token_obj , _ = Token.objects.get_or_create(user=user)
        refresh = RefreshToken.for_user(user)


        return Response({'status':200,
        'payload': serializer.data,
        'refresh': str(refresh),
        'access': str(refresh.access_token), 'message':'Your data is saved'})





class StudentAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        student_objs = student.objects.all()
        serializer = studentserializers(student_objs, many=True)
        print(request.user)
        return Response({'status': 200, 'payload': serializer.data})


    def post(self, request):
        data = request.data 
        serializer = studentserializers(data = request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403, 'errors':serializer.errors , 'message':'something went wrong'})
        serializer.save()

        # print(data)
        return Response({'status': 200, 'payload': data, 'message': 'you sent'})

    def put(self, request):
        pass

    def patch(self, request):
        try:
            student_objs = student.objects.get(id=request.data['id'])
            serializer = studentserializers(student_objs, data = request.data, partial=True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403, 'errors':serializer.errors , 'message':'something went wrong'})
            serializer.save()
            return Response({'status': 200, 'payload': serializer.data, 'message': 'Updated'})
        
        except Exception as e:
            return Response({'status':403, 'message':'Invalid id'})

    def delete(self, request):
        try:
            student_objs = student.objects.get(id= request.data['id'])
            student_objs.delete()
            return Response({'status':200, 'message': "Deleted"})
        except Exception as e:
            print(e)
            return Response({'status':403, 'message': "invalid id"})



class GeneratePdf(APIView):
    def get(self, request):

        return Response({'status':200})



# @api_view(['Get'])
# def home(request):
#     student_objs = student.objects.all()
#     serializer = studentserializers(student_objs, many=True)
#     return Response({'status': 200, 'payload': serializer.data})

# @api_view(['Post'])
# def post(request):
#     data = request.data 
#     serializer = studentserializers(data = request.data)

#     if not serializer.is_valid():
#         print(serializer.errors)
#         return Response({'status':403, 'errors':serializer.errors , 'message':'something went wrong'})
#     serializer.save()

#     # print(data)
#     return Response({'status': 200, 'payload': data, 'message': 'you sent'})


# @api_view(['Put'])
# def update_student(request, id):
#     try:
#         student_objs = student.objects.get(id=id)
#         serializer = studentserializers(student_objs, data = request.data, partial=True)
#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status':403, 'errors':serializer.errors , 'message':'something went wrong'})
#         serializer.save()
#         return Response({'status': 200, 'payload': serializer.data, 'message': 'you sent'})
    
#     except Exception as e:
#         return Response({'status':403, 'message':'Invalid id'})


# @api_view(['DELETE'])
# def delete_student(request, id):
#     try:
#         student_objs = student.objects.get(id=id)
#         student_objs.delete()
#         return Response({'status':200, 'message': "Deleted"})
#     except Exception as e:
#         print(e)
#         return Response({'status':403, 'message': "invalid id"})

