import logging

logger = logging.getLogger(__name__)
import uuid

from django.core.validators import MinLengthValidator, RegexValidator
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from rest_framework.renderers import JSONRenderer
from django.contrib.gis.geos import Point



class Location(models.Model):
    address = models.CharField(max_length=20, blank=False)
    lat = models.FloatField()
    lon = models.FloatField()

    def __str__(self):
        return self.address

    def get_location(self):
        return Point(float(self.lon), float(self.lat))  # lon first

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField('Name', max_length=40)
    username = models.EmailField(blank=False, unique=True) #TODO: do not cascade delete on model
    location = models.ForeignKey('Location',on_delete=models.CASCADE, null=True, blank=True) #country
    is_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    password_recently_reset = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Post(models.Model):
    post_title = models.CharField('Activation Token', max_length=40)
    text = models.CharField('Activation Token', max_length=40)
    tags = models.CharField('Activation Token', max_length=40)

class Tag(models.Model):
    tag_name = models.CharField('Activation Token', max_length=40)


class ActivationToken(models.Model):
    POSSIBLE_STATUSES = (
        ('A', 'ACTIVE'),
        ('E', 'EXPIRED')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tokenuser')
    token = models.CharField('Activation Token', max_length=40)
    status = models.CharField(max_length=1, choices=POSSIBLE_STATUSES, default='A')
    date_added = models.DateTimeField('date', default=timezone.now, null=True)

    def __str__(self):
        return "{}'s activation token".format(self.user.name)
