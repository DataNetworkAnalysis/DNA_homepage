from django.urls import path
from . import views

app_name = 'test2'
urlpatterns = [
    path('',views.index, name='index')
]