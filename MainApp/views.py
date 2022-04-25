from django.shortcuts import render
from .models import Topic

# Create your views here.

def index(request):
    return render(request, 'MainApp/index.html')


def topics(request):
    topics = Topic.objects.all()

    context = {'topics':topics}                 #the key is what you need to use in the html template, the value is used in the view file 

    return render(request, 'MainApp/topics.html', context)

