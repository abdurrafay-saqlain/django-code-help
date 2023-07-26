from django.shortcuts import render
from rest_framework import  permissions

from .models import *
from rest_framework.views import APIView

from rest_framework.permissions import AllowAny
from .serializers import *
from rest_framework.response import Response
# Create your views here.
class RegisterAPI(APIView):
    permission_classes = [permissions.AllowAny]
    
    #   queryset=User.objects.all()
    #   permission_classes = [AllowAny]
    #   serializer_class=UserSerializer
      
      
 
    def post(self, request):
        
      
        
        print(request.data)
        serializer = UserSerializer(data=request.data,context={
            'request':request
        })
        if serializer.is_valid():
            
           
            serializer.save()
            return Response({
                "data": serializer.data
            })
        else:
            print(serializer.errors)
            return Response({
                "errors": serializer.errors
            })
        
    
      
class FreelancerRegistration(APIView):
    # queryset=Freelancer.objects.all()
    # permission_classes = [AllowAny]
    # serializer_class=FreelancerSerializer
    def post(self,request):
    
      
        serializer=FreelancerSerializer(data=request.data)
        # import pdb 
        # pdb.set_trace()
        
        if serializer.is_valid():
            serializer.save()
            user=Freelancer.objects.get(email=request.data['email'])
            serialize_user=ReadUserSerializer(user)
            
            print(serializer)
            return Response({
                'data':serialize_user.data
            })
            
             
        else:
            print(serializer.errors)
        return Response({
               
                'errors':'Invalid data'
            })
        
        
    def get(self,request):
          freelancer=Freelancer.objects.all()
          serializer=ReadUserSerializer(freelancer,many=True)
          return Response({
                        
              "data":serializer.data,
              
          })
    
          
        
class EducationAPI(APIView):
    # queryset=Education.objects.all()
    # permission_classes = [AllowAny]
    # serializer_class=EducationSerializer
    def post(self,request):
        serializer=EducationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data':serializer.data
            })
        else:
            return Response({
                'errors':'Invalid data'
            })
      
class SkillsAPI(APIView):
    # queryset=Skills.objects.all()
    # permission_classes = [AllowAny]
    # serializer_class=SkillsSerializer
    def post(self,request):
        serializer=SkillsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data':serializer.data
            })
        else:
            return Response({
                'errors':'Invalid data'
            })
      
        
      
        
class CertificationAPI(APIView):
    # queryset=Certification.objects.all()
    # permission_classes = [AllowAny]
    # serializer_class=CertificationSerializer
    def post(self,request):
        serializer=CertificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data':serializer.data
            })
        else:
            return Response({
                'errors':'Invalid data'
            })
            
class PortfolioAPI(APIView):
    # queryset=Portfolio.objects.all()
    # permission_classes = [AllowAny]
    # serializer_class=PortfolioSerializer
    def post(self,request):
        serializer=CertificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data':serializer.data
            })
        else:
            return Response({
                'errors':'Invalid data'
            })
      
    
class PortfolioAPI(APIView):
    # queryset=Portfolio.objects.all()
    # permission_classes = [AllowAny]
    # serializer_class=PortfolioSerializer
    def post(self,request):
        serializer=CertificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'data':serializer.data
            })
        else:
            return Response({
                'errors':'Invalid data'
            })
      
    