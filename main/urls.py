# main urls
from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('user/', test),
    path('post/<int:pk>/', показать_пост, name='show-post'),
    path('reg/', reg, name='reg'),
    path('create-post/', create_post, name='create-post'),
]
