from django.urls import path
from . import views

app_name ='test3'
urlpatterns = [
    path('', views.index, name='index'),
    path('testtt',views.test_index, name='test')
]