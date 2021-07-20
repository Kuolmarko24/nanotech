from django.db import models

# Create your models here.

class Product(models.Model):
    item = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True)
    quantity = models.IntegerField(null=True)
    price = models.FloatField(null=True)
    specs = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.item
class Promotion(models.Model):
    STATUS = (
        ('On promotion', 'On promotion'),
        ('Upcoming', 'Upcoming'),
    )
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    promo_name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.promo_name

