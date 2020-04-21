
# Create your models here.
from django.db.models import *

# Create your models here.


class Skill(Model):
    # SKILLS_LIST = TextChoices('Compositing', '3D')
    objects = Manager()
    skill = CharField(max_length=200)


class Collaborator(Model):
    objects = Manager()
    name = CharField(max_length=200)
    email = CharField(max_length=200)
    phone = CharField(max_length=200)
    position = CharField(max_length=200, blank=True)
    availability = CharField(max_length=200, blank=True)
    main_skills = ManyToManyField(Skill)
    # secondary_skills = CharField(max_length=200, blank=True)
    # showreel = CharField(max_length=200)
    # worked_on = CharField(max_length=200)
    # connection = CharField(max_length=200)


