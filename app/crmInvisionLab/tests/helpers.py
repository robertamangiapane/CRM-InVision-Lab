from ..models import Collaborator, Skill


def create_collaborator1_3D_for_test():
    skill = Skill(name="3D")
    skill.save()
    collaborator = Collaborator(name="First collaborator",
                                email="email",
                                phone="5555555555",
                                position="Rome",
                                availability="Weekend")
    collaborator.save()
    collaborator = Collaborator.objects.get(name="First collaborator")
    collaborator.main_skills.add(skill)
    collaborator.save()

    return collaborator


def create_collaborator2_compositing_for_test():
    skill = Skill(name="Compositing")
    skill.save()
    collaborator = Collaborator(name="Second collaborator",
                                email="email",
                                phone="5555555556",
                                position="London",
                                availability="Always")
    collaborator.save()
    collaborator = Collaborator.objects.get(name="Second collaborator")
    collaborator.main_skills.add(skill)
    collaborator.save()

    return collaborator


def create_skill_compositing_for_test():
    skill = Skill(name="Compositing")
    skill.save()
    return skill


def create_skill_3D_for_test():
    skill = Skill(name="3D")
    skill.save()
    return skill


def create_wrong_skill_for_test():
    skill = Skill(name="Wrong")
    skill.save()
    return skill
