from django.db import models

# Create your models here.
from django.db.models import *

# Create your models here.


class Collaborator(Model):
    objects = Manager()
    name = CharField(max_length=200)
    email = CharField(max_length=200)
    phone = CharField(max_length=200)
    position = CharField(max_length=200, default="Remote", blank=True)
    availability = CharField(max_length=200, default="Always", blank=True)
    main_skills = CharField(max_length=200, blank=True)
    secondary_skills = CharField(max_length=200, blank=True)
    # showreel = CharField(max_length=200)
    # worked_on = CharField(max_length=200)
    # connection = CharField(max_length=200)

