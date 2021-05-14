from django.urls import path, include
from . import views

app_name = 'students'

urlpatterns = [
   path('reg/',views.regStudent, name ='reg'),
   path('regCon/',views.regConStudent, name = 'regCon'),
   path('all/',views.reaStudentAll, name = 'stuAll'),
   path('<str:name>/det/',views.detStudent, name = 'stuDet'),
   path('<str:name>/mod/',views.reaStudentOne, name = 'stuMod'),
   path('modCon/',views.modConStudent, name = ' modCon'),
  
]
  