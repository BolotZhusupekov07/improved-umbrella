from django.db import models
from django.db.models.deletion import CASCADE



class Category(models.Model):
    name = models.CharField(max_length=200)
    imgpath = models.CharField(max_length=200)


class Branch(models.Model):
    latitude = models.CharField(max_length=200)
    longitude = models.CharField(max_length=200)
    address = models.CharField(max_length=300)


class Contact(models.Model):
    PHONE = 'PH'
    FACEBOOK = 'FA'
    EMAIL = 'EM'
    choices = [
            (PHONE, 'PHONE'),
            (FACEBOOK, 'FACEBOOK'),
            (EMAIL, 'EMAIL')
    ]
    type = models.CharField(max_length=2,choices=choices,default=PHONE)
    value = models.CharField(max_length=200)


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    logo = models.CharField(max_length=200)
    contacts = models.ManyToManyField(Contact)
    branches = models.ManyToManyField(Branch)