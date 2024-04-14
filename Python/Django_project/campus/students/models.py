from django.db import models


class Contact_Data(models.Model):
    username = models.CharField(max_length=125)
    useremail = models.CharField(max_length=125)
    phone = models.CharField(max_length=125)
    desc = models.TextField()
    date = models.DateField()
    
    def __str__(self):
       return self.username    


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
