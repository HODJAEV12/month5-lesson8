from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=250, verbose_name='Имя')
    last_name = models.CharField(max_length=250, verbose_name='Фамилия')
    age = models.IntegerField(verbose_name='Возраст')