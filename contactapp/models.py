from django.db import models

# Create your models here.
class contactmodel(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    mobile=models.CharField(max_length=100)
    message=models.TextField(max_length=100)
    status=models.BooleanField(default=False)

class videomodel(models.Model):
    video=models.FileField(upload_to='videos_uploaded',null=True)
    
 