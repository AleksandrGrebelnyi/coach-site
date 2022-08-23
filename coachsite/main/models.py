from django.db import models

# Create your models here.


class ForWhom(models.Model):
    name_of_for_whom = models.CharField(max_length=50, default='')
    for_whom = models.TextField(max_length=500)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.for_whom}'

    class Meta:
        ordering = ['time_update']


class CustomerResult(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.title}'


class Tariffs(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1500)

    def __str__(self):
        return f'{self.title}'


class AboutMe(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1500)

    def __str__(self):
        return f'{self.title}'


class Contacts(models.Model):
    title = models.CharField(max_length=200, default='')
    phone = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.title}'