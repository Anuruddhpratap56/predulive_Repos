from django.db import models

class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    mobile=models.CharField(max_length=13)
    email_sub=models.CharField(max_length=100)
    description=models.TextField()
