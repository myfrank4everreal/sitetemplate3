from django.urls import path
from . import views


urlpatterns = [
    path('', views.demoindex, name='demoindex'),
#     path('demoaboutus', views.demoabout, name='demoabout'),
]
