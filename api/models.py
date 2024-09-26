from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.




# Model of Cart
class Cart(models.Model):
    cart_items = JSONField(default=[ ], blank=True)

# Model of Category
class Category(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
