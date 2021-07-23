from django.db import models


# Create your models here.

class Products(models.Model):
  title = models.CharField(max_length=500)
  price = models.FloatField()
  discounted_price = models.FloatField()
  category = models.CharField(max_length=500)
  description = models.TextField()
  image = models.CharField(max_length=500)

  class Meta:
    verbose_name = 'Product'
    verbose_name_plural = 'Products'

  def __str__(self):
    return self.title