from django.urls import path
from shop_app.views import index,persons

urlpatterns = [
    path('index',index,name='index'),
    path('person',persons,name='index')


]
