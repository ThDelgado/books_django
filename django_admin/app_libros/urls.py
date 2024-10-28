from . import views
from django.urls import path, include

urlpatterns = [
    path('newbook/', views.newbook, name= 'newbook'),
    path('listbook/', views.listbook, name= 'listbook'),
]



