from django.shortcuts import render
from django.http import HttpResponse

# Create your views here


def multi(request):
    if request.method=="POST":
        foods=request.POST.getlist("food")
        languages=request.POST.getlist("language")
        return HttpResponse("<h1>{}{}<h1>".format(foods,languages))
    return render(request,'multiselect.html')

from django.core.files.storage import FileSystemStorage

def img_upld(request):
    if request.method=="POST" and request.FILES:
        image=request.FILES['sam']
        fs=FileSystemStorage()
        fs.save(image.name,image)
                
    return render(request,"img_upld.html")