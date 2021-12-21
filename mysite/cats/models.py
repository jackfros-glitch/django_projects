from django.db import models

# Create your models here.
class Breed(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Cat(models.Model):
    nickname = models.CharField(max_length=200,)
    weight = models.FloatField()
    foods = models.CharField(max_length=200, null=True)
    breed = models.ForeignKey('Breed', on_delete=models.CASCADE, null=False)


    def __str__(self):
        return self.nickname