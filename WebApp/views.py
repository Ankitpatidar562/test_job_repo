from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import generics
from WebApp.models import ProjectHire,ProjectDeveloper
from WebApp.serializers import ProjectHireSerializer1,ProjectHireSerializer2,ProjectDeveloperSerializer,UserProjectDetailViewSerializer
# Create your views here.

def Home(request):
    return HttpResponse("Test")

class Project_Hire_View(generics.ListCreateAPIView):
    queryset = ProjectHire.objects.all()
    serializer_class = ProjectHireSerializer1
    

class Project_Hire_Detail_View(generics.ListAPIView):
    queryset = ProjectHire.objects.all()
    serializer_class = ProjectHireSerializer2

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        project_name = self.kwargs['project_name']
        return ProjectHire.objects.filter(project_name=project_name)
    
    
class Project_Developer_View(generics.ListCreateAPIView):
    queryset = ProjectDeveloper.objects.all()
    serializer_class = ProjectDeveloperSerializer
    
    
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated    
class UserProjectDetailView(generics.ListAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes= [IsAuthenticated]
    
    serializer_class = ProjectDeveloperSerializer
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authen1ticated user.
        """
        user = self.request.user
        #username=self.kwargs['username']
        return ProjectDeveloper.objects.filter(developer__developer_name__username=user)

from django.contrib.auth.models import User
from rest_framework.views import APIView

class UserView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes= [IsAuthenticated]
    
    def get(self,request):
        user=User.objects.filter(id=request.user.id).first()
        if user:
            ser =UserProjectDetailViewSerializer(user, context={'user':user})
            return Response(ser.data)
        return Response({'message':'no data found'})
            
    

# class UserView(generics.RetrieveAPIView):
#     authentication_classes = [SessionAuthentication, BasicAuthentication]
#     permission_classes= [IsAuthenticated]
#     lookup_field = [self.get_serializer_context()['user']]
    
#     serializer_class = ProjectDeveloperSerializer2
#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         context.update({"user": self.request.user})
#         return context
#     # def get_queryset(self):
#     #     """
#     #     This view should return a list of all the purchases
#     #     for the currently authenticated user.
#     #     """
#     #     user = self.request.user
    #     #username=self.kwargs['username']
    #     return User.objects.filter(id=user.id).first()
    
    
    
# class Project_User_View(generics.ListAPIView):
#     #queryset = User.objects.all()
#     serializer_class = UserSerializer
#     def get_queryset(self):
#         """
#         This view should return a list of all the purchases
#         for the currently authenticated user.
#         """
#         user = self.request.user
#         return User.objects.filter(username=user)
    
    
    
    
    
    
    
    
    
    
    
"""from django.http import JsonResponse
from rest_framework.views import APIView
class Project_User_View(APIView):
    #queryset = ProjectDeveloper.objects.all()
    #serializer_class = ProjectDeveloperSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes= [IsAuthenticated]
    
    def get(self, request, format=None):
        user =self.request.user
        data={}
        p = []
        #usernames = [user.username for user in User.objects.all()]
        project = ProjectDeveloper.objects.filter(developer__developer_name__username=user)
        for i in project:
            #print(i.id)
            #print(i.project_hire.project_name)
            l = i.project_hire.project_name
            f =i.role.all()
            for r in f:
                print(r)
            #print(f)
            p.append(l)
        data['project Name']=p
        print(data)
            
            #lan = [str(lang) for lang in f]
        serailizer = ProjectDeveloperSerializer(project,many=True).data
        return Response(serailizer)
        
        """

from datetime import datetime
import time
#SQl Query
import pandas as pd

from django.db import connection
def call_sql(request):
    with connection.cursor()  as cursor:
       
        cursor.execute("select * from WebApp_roll")
        row = cursor.fetchall()
        d = pd.DataFrame(row)
        print(d)

        #Dict
        # columns = [col[0] for col in cursor.description]
        # row =  [dict(zip(columns, row)) for row in cursor.fetchall()]   
        #print(row)
    return HttpResponse(row)
