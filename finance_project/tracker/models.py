from django.db import models

# Create your models here.
class Transaction(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20)
    description = models.TextField(help_text="Please enter a description of the transaction")
    pass
