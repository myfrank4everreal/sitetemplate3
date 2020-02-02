from django.shortcuts import render, redirect
from .models import Article



def index(request):
    article_list = Article.objects.all()
    
    context = {'article_list':article_list}
    return render(request, 'blog/index.html', context)





def viewBlog(request, article_id):
    article_list = Article.objects.get(pk=article_id)
    
    context = {'article_list':article_list}
    return render(request, 'blog/viewBlog.html', context)


    



def services(request):
    #  myobject = modeltemp.objects.all()
    context = {}
    return render(request, 'blog/services.html', context)




