from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin
# Register your models here.
#


admin.site.register(models.Comment, MPTTModelAdmin)
admin.site.register(models.Rating)
admin.site.register(models.Category)
admin.site.register(models.Article)
