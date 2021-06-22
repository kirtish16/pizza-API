from django.db import models

#Pizza model containing the type, size of pizza and the topping on pizza
class Pizza(models.Model):
    type = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    toppings = models.CharField(max_length=50)
