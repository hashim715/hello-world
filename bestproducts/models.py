from django.db import models

# Create your models here.
class Products (models.Model):
	title = models.TextField()
	decription = models.TextField()
	price = models.TextField()
