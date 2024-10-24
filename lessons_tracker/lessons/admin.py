# Register your models here.
from django.contrib import admin
from django.db.models import Model
from . import models

for obj_name in dir(models):
    obj = getattr(models, obj_name)
    if isinstance(obj, type) and issubclass(obj, Model):
        admin.site.register(obj)
