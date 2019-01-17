from django.db import models
from datetime import datetime
from volunteers.models import Volunteer


class Pet(models.Model):
    volunteer = models.ForeignKey(Volunteer, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
