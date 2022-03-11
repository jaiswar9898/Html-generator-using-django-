from django.urls import path
from pdapp import views


urlpatterns = [ 
    path('',views.home,name='home'),
   
    
]
