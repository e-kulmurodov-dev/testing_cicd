from django.db.models import Model, ForeignKey, CASCADE
from django.forms import CharField


# Create your models here.

class Category(Model):
   name = CharField(max_length=155)

class Product(Model):
   name = CharField(max_length=155)
   category = ForeignKey('apps.Category', CASCADE)
