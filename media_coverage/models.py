from django.db import models

class news(models.Model):
    headLine=models.CharField(max_length=100)
    description=models.TextField()
    image=models.FileField(upload_to="media_coverage/",max_length=250,null=True,default=None)


class achievements(models.Model):
    date=models.CharField(max_length=15)
    heading=models.CharField(max_length=50)
    description=models.TextField()
    image=models.FileField(upload_to="media_coverage/",max_length=250,null=True,default=None)