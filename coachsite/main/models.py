from django.db import models
from django.core.validators import RegexValidator

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


class UserReservation(models.Model):
    name = models.CharField(max_length=50)
    email_re = RegexValidator(regex=r'(^[A-Za-z0-9]+[\w_]+.[\w_]+@[0-9A-Za-z]+\.[a-z]{2,7}$)',
                              message='Check your email or put another')
    mobile_re = RegexValidator(regex=r'^((\+?\d{3}[- .]?)\d{7,13}$)', message='Phone in format xxx xxx xxxx')
    email = models.EmailField(max_length=50, validators=[email_re])
    phone = models.CharField(max_length=20, validators=[mobile_re])
    message = models.TextField(max_length=200, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date', '-is_processed')

    def __str__(self):
        return f'{self.name}, {self.phone}, {self.email}: {self.message[:50]}'