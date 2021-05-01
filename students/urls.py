from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'students'
urlpatterns = [
   path('reg/',views.regStudent, name ='reg'),
   path('regCon/',views.regConStudent, name = 'regCon'),
   path('all/',views.reaStudentAll, name = 'stuAll'),
]
  