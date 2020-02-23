from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    city = models.CharField(max_length = 100)
    state = models.CharField(max_length = 50)
    zip_code = models.CharField(max_length = 10)
    phone_number = models.CharField(max_length = 10)

    def __str__(self):
        return f'{self.name} - {self.user}'

class Job(models.Model):
    business = models.ForeignKey(Business, on_delete= models.CASCADE)
    title = models.CharField(max_length = 200)
    description = models.TextField(blank = True)
    new = models.BooleanField(default = True)

    def __str__(self):
        return f'{self.title} - {self.business}'

class JobSeekerEmail(models.Model):
    email = models.EmailField(max_length = 100, blank = False)
    
