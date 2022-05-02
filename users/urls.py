from django.urls import path, inlcude 

app_name = 'users'

urlpatterns = [
    path('',inlcude('django.contrib.auth.urls')),
]
