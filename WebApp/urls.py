from django.urls import path,re_path
from WebApp import views
urlpatterns = [
    path('home',views.Home),
    path('project_hire/',views.Project_Hire_View.as_view()),   #Task
    re_path('^project_hire/(?P<project_name>.+)/$',views.Project_Hire_Detail_View.as_view()), #Task
    path('project_developer',views.Project_Developer_View.as_view()),
    path('user',views.UserProjectDetailView.as_view()),
    path('user_project',views.UserView.as_view()),   #Task
    #path('project_user',views.Project_User_View.as_view()),
    path('sql',views.call_sql),
]

