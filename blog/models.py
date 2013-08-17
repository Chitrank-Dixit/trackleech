from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class posts(models.Model):
    # This is a post model used in the Django Admin Panel     
    author = models.CharField(max_length = 30)
    title = models.CharField(max_length = 100)
    bodytext = models.TextField()
    timestamp = models.DateTimeField()

'''
class signup(models.Model):
    # This is a Sign up model that does the signup of the person to the site
    username = models.CharField(max_length = 30)
    email = models.CharField(max_length = 40)
    password = models.CharField(max_length = 20)
    last_login= models.DateTimeField()
    date_joined= models.DateTimeField()
'''    
    
    




