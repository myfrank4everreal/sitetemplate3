from django.shortcuts import render
from .models import modeltemp

def demoindex(request):
    myobject = modeltemp.objects.all()
    context = {'myobject':myobject}
    return render(request, 'myapp/demoindex.html', context)



# this is for the about page
def demoabout(request):
    context = {}
    return render(request, 'myapp/demoabout.html', context)
