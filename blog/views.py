from django.shortcuts import render



def home(request):
    #  myobject = modeltemp.objects.all()
    context = {}
    return render(request, 'blog/home.html', context)



def services(request):
    #  myobject = modeltemp.objects.all()
    context = {}
    return render(request, 'blog/services.html', context)




