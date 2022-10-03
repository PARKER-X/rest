from django.contrib import admin

from home.models import student
from .models import *

# Register your models here.
admin.site.register(student)
admin.site.register(Book)
admin.site.register(Category)