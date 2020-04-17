from .models import Collaborator
from .models import Skill


def create_collaborator1_for_test():
    collaborator = Collaborator("1", "First collaborator", "email", "5555555555", "Rome", "Weekend")
    collaborator.save()
    return collaborator

def create_collaborator2_for_test():
    collaborator = Collaborator("2", "Second collaborator", "email", "5555555556", "Rome", "Always")
    collaborator.save()
    return collaborator

def create_skill1_for_test():
    skill = Skill("1", "Compositing")
    skill.save()
    return skill

def create_skill2_for_test():
    skill = Skill("2", "3D")
    skill.save()
    return skill
