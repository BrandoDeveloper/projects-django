from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class Video(models.Model):
    title=models.CharField(max_length=50)
    caption=models.CharField(max_length=100)
    video=models.FileField(upload_to="video/%y")
    
    def __str__(self):
        return self.caption
