from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.user)
admin.site.register(models.postData)
admin.site.register(models.reviewData)