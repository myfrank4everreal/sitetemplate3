from django.shortcuts import render
from .models import modeltemp

def index(request):
    myobject = modeltemp.objects.all()
    context = {'myobject':myobject}
    return render(request, 'myapp/index.html', context)



# this is for the about page
def about(request):
    context = {}
    return render(request, 'myapp/about.html', context)
