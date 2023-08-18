from django.db import models

class campaigns(models.Model):
    day=models.CharField(max_length=2)
    m_y=models.CharField(max_length=10)
    heading=models.CharField(max_length=50)
    description=models.TextField()
    image=models.FileField(upload_to="camapigns/",max_length=250,null=True,default=None)