from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.upload,name='home'),
    path('delete_image/<int:pk>/',views.delete_img,name='delete_image'),
    
]
