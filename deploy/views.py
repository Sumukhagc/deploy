from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
def home(request):
    return render(request,'home.html')

def predict(request):
    fname=request.GET['fname']
    return render(request,'predict.html',{'fname':fname})