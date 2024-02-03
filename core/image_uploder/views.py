from django.shortcuts import render,get_object_or_404,redirect
from .models import Image_uploder
from .form import Image_form
# Create your views here.


def upload(request):
    fm=Image_form()
    im=Image_uploder.objects.all()
    
    if request.method == "POST":
        fm=Image_form(request.POST,request.FILES)
        if fm.is_valid():
            fm.save()
    
    context={
        'form':fm,
        "img":im,
    }
    return render(request,'upload_image.html',context)

def delete_img(request,pk):
    img=get_object_or_404(Image_uploder,pk=pk)
    img.delete()
    return redirect('home')
    