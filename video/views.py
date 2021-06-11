from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Video
# Create your views here.

def blog(request):
    video =Video.objects.all()
    return render(request,"video.html", {"video":video})
