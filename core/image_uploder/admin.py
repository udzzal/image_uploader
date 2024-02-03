from django.contrib import admin
from .models import Image_uploder
# Register your models here.


class Dis(admin.ModelAdmin):
    list_display=['id','image','date']
    
admin.site.register(Image_uploder,Dis) 