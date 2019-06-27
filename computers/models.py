from django.db import models
from django.urls import reverse

# Create your models here.

class Computer(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('computers:computer_edit', kwargs={'pk': self.pk})


class OS(models.Model):
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    os_type = models.CharField(max_length=255)


class Producer(models.Model):
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    country = models.CharField(max_length=255)
