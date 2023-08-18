from django.db import models

class innovation(models.Model):
    published_by=models.CharField(max_length=15)
    heading=models.CharField(max_length=100)
    date=models.CharField(max_length=8)
    image=models.FileField(upload_to="innovations/",max_length=250,null=True,default=None)
