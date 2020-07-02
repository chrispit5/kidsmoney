from django.db import models

# Create your models here.


class Person(models.Model):
	name		= models.CharField(max_length=4)
	startingbalance	= models.IntegerField()

	def __str__(self):
		return self.name




class Expenses(models.Model):
	name 		= models.ForeignKey(Person, related_name='expenses', on_delete=models.CASCADE)
	item		= models.CharField(max_length=20)	
	amount		= models.IntegerField()
	exdate		= models.DateField()



