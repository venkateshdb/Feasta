from django.db import models

# Create your models here.

class Record(models.Model):
    username = models.CharField(max_length= 20, blank = True)
    password = models.CharField(max_length = 15, blank= True)
    email = models.EmailField(max_length = 20, blank = True)
    phone = models.CharField(max_length = 10, blank = True)
    first_name = models.CharField(max_length = 30, blank = True)
    last_name = models.CharField(max_length = 30, blank = True)
    last_login = models.DateTimeField(blank = True, auto_now_add= True)
    is_active = models.BooleanField(blank=True)
    date_created = models.DateField(auto_now_add=True)

class ShopOwner(Record):
    Shop_Name = models.CharField(max_length = 30, blank = True)
    Address = models.CharField(max_length=150, blank = True)

class User(Record):
    College = models.CharField(max_length=40, blank = True)
    Stay = models.CharField(max_length=150, blank=True)