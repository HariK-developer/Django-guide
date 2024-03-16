from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .helpers import encrypt_data

# Create your models here.


class Foo(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """

    name = models.CharField(max_length=100)
    is_true = models.BooleanField(default=False)


class Person(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=277)


class BankDetails(models.Model):
    """_summary_

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=100)
    
    def save(self, *args, **kwargs):
        self.account_number = encrypt_data(data=self.account_number)
        return super().save(*args, **kwargs)


class SoftDeleteManager(models.Manager):
    """
    Returns a QuerySet of all objects in the database that have not been marked for deletion.
    """

    def get_queryset(self):
        """
        Returns a QuerySet of all objects in the database that have not been marked for deletion.
        """
        return super().get_queryset().filter(delete=False)


class Student(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    delete = models.BooleanField(default=False)

    objects = SoftDeleteManager()


class Author(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """

    name = models.CharField(max_length=255)


class Book(models.Model):
    """_summary_

    Args:
        models (_type_): _description_
    """

    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


class BankAccount(models.Model):
    account_number = models.CharField(max_length=255,unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    
    

# Custom Managers 


class AuthorManager(models.Manager):
    def get_queryset(self):
        """
        Returns a QuerySet of all objects in the database that have  marked for role A.
        """
        return super().get_queryset().filter(role='A')


class EditorManager(models.Manager):
    def get_queryset(self):
        """
        Returns a QuerySet of all objects in the database that have  marked for role E.
        """
        return super().get_queryset().filter(role='E')
    
    
class People(models.Model):
    choices = (("A","Author"),("E","Editor"))
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=1,choices=choices)
    
    objects = models.Manager() # default manager
    
    authors = AuthorManager() # author manager
    
    editors = EditorManager() # editor manager
    
    

# This will return person whose role is author
People.authors.all()

# This will return whose role is editor
People.editors.all()

# This will return all person whose role is either author or editor
Person.objects.all()


# How to use related_name 

class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField(max_length=500)
    
    
# the default related_name should be 

""" user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='address_set') """

# how to override the default related_name

""" user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_address')"""

# Validators

# Here MinValueValidator is Django's Built-in validator
class Things(models.Model):
    count = models.PositiveIntegerField(validators=[MinValueValidator])
    

# create a custom validator

def validate_even(value: int) -> None:
    """
    Validates that the input value is an even number.

    Args:
        value (int): The value to be validated.

    Raises:
        ValidationError: If the value is not an even number.

    """
    if value % 2!= 0:
        raise ValidationError(
            _("Value must be a even number"), code="invalid"
        )


class Stuff(models.Model):
    count = models.PositiveIntegerField(validators=[validate_even])
    
    
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        
        
class PythonModel(BaseModel):
    language = models.CharField(max_length=50)
    version = models.DecimalField(decimal_places=3,max_digits=3)
    
    class Meta:
        verbose_name_plural = _('Python')
        ordering = ['-created_at']