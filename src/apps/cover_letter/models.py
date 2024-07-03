from django.db import models

from smart_cv_server import settings

User = settings.AUTH_USER_MODEL

class CoverLetter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    job_description = models.TextField(max_length=1000,null=True,blank=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=255)
    experience = models.TextField(max_length=1000,default="",null=True,blank=True)
    body = models.TextField(blank=True,null=True)


    def __str__(self):
        return f"{self.job_title} at {self.company_name} - {self.name}"
