from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('student/' ,StudentAPI.as_view()),
    # path('', home),
    # path('post/', post),
    # path('update-post/<id>/', update_student),
    # path('delete_post/<id>/', delete_student),
    path('get_book/', get_book),
    path('register/',RegisterUser.as_view())
]
