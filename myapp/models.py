from django.db import models

# Create your models here.


class Expense(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    category = models.CharField(max_length=50)
    # auto_now=True means that the date will be automatically set to the current date when object made
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name