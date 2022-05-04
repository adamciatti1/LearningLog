from django.urls import path, inlcude 

app_name = 'users'

from . import views 


app_name = 'users' 

urlpatterns = [
    # Include default auth urls
    path('',inlcude('django.contrib.auth.urls')),
    # Registration page
    path('register/', views.register, name='register'),
]
