# main urls
from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('user/', test),
    path('post/<int:pk>/', показать_пост,)
]
