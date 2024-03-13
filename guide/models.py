from django.db import models
from django_seed import Seed
from django.contrib.auth.models import User
from .helpers import encrypt_data
# Create your models here.


class Foo(models.Model):
    name = models.CharField(max_length=100)
    is_true = models.BooleanField(default=False)
    
    
class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=277)
    

class BankDetails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    account_number = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        self.account_number = encrypt_data(data = self.account_number)
        return super().save(*args, **kwargs)
    
    
seeder = Seed.seeder()

seeder.add_entity(Person, 5)
seeder.execute()