import os
from django.db import models
from core import models as core_models
from django_countries.fields import CountryField
from users import models as user_models

class Item(core_models.TimeStampedModel):
    
    """ Abstract Item """

    pass

    class Meta:
        abstract = True

class Room(core_models.TimeStampedModel):

    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    cuntry = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name