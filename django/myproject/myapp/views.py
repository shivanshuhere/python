from django.shortcuts import render
from .models import MyModel
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

infos = MyModel.objects.all()

def info(request):
    return render(request, 'info.html',{"info":infos})