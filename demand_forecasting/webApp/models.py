from django.db import models

class DF_Model(models.Model):
    warehouse = models.CharField(max_length=100)
    product_category = models.CharField(max_length=100)
    date = models.DateField()