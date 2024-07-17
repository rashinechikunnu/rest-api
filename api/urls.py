from django.urls import path
from shop_app.views import index,persons,classperson

urlpatterns = [
    path('index',index,name='index'),
    path('person',persons,name='index'),
    path('personclass',classperson.as_view(),name="personclass")


]
