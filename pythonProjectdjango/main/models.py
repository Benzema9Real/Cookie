from django.db import models


class MyModel(models.Model):
    my_file = models.FileField(upload_to='files/')
    my_image = models.ImageField(upload_to='images/')


class Product(models.Model):
    product = models.CharField('Название', max_length=50)
    description = models.CharField('Описание', max_length=50)
    price = models.IntegerField('Цена')
    my_image = models.ImageField(upload_to='images/')


def __str__(self):
    return self.author_name
