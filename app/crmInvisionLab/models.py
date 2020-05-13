from django.db.models import *
from phonenumber_field.modelfields import PhoneNumberField


class Skill(Model):
    objects = Manager()
    name = CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Job(Model):
    objects = Manager()
    name = CharField(max_length=200)
    preview = URLField(max_length=200, blank=True)
    link = URLField(max_length=200, blank=True)
    ended = BooleanField(default=False)

    def __str__(self):
        return self.name


class Collaborator(Model):
    objects = Manager()
    name = CharField(max_length=200, unique=True)
    email = EmailField(max_length=200)
    phone = PhoneNumberField(max_length=200, region='GB')
    position = CharField(max_length=200, blank=True)
    availability = CharField(max_length=200, blank=True)
    main_skills = ManyToManyField(Skill, related_name="main_skills", blank=True)
    secondary_skills = ManyToManyField(Skill, related_name="secondary_skills", blank=True)
    showreel = URLField(max_length=200, blank=True)
    ongoing_projects = ManyToManyField(Job, related_name="ongoing_projects", blank=True)
    past_collaborations = ManyToManyField(Job, related_name="past_collaborations", blank=True)
