from ..models import Collaborator, Skill


def create_collaborator1_skill1_for_test():
    skill = Skill(name="skill one")
    skill.save()
    collaborator = Collaborator(name="First collaborator",
                                email="email",
                                phone="5555555555",
                                position="Position",
                                availability="Availability")
    collaborator.save()
    collaborator = Collaborator.objects.get(name="First collaborator")
    collaborator.main_skills.add(skill)
    collaborator.save()

    return collaborator


def create_collaborator2_skill2_for_test():
    skill = Skill(name="skill two")
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

def create_collaborator3_with_main_and_secondary_skills_for_test():
    skill = Skill(name="skill one")
    skill.save()
    skill2 = Skill(name="Secondary")
    skill2.save()

    collaborator = Collaborator(name="Third collaborator",
                                email="email",
                                phone="5555555555",
                                position="Position",
                                availability="Availability")
    collaborator.save()
    collaborator = Collaborator.objects.get(name="Third collaborator")
    collaborator.main_skills.add(skill)
    collaborator.secondary_skills.add(skill2)
    collaborator.save()

    return collaborator


def create_skill2_for_test():
    skill = Skill(name="skill two")
    skill.save()
    return skill


def create_skill1_for_test():
    skill = Skill(name="skill one")
    skill.save()
    return skill


def create_wrong_skill_for_test():
    skill = Skill(name="Wrong")
    skill.save()
    return skill
