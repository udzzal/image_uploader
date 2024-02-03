from django.db import models

# Create your models here.
class Image_uploder(models.Model):
    image=models.ImageField(upload_to='image')
    date=models.DateTimeField(auto_now_add=True)
    
    
    