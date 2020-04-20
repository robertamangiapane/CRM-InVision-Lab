from .models import Collaborator, Skill, CollaboratorSkill


def create_collaborator1_3D_for_test():
    collaborator = Collaborator(name="First collaborator",
                                email="email",
                                phone="5555555555",
                                position="Rome",
                                availability="Weekend")
    collaborator.save()
    skill = Skill(skill="3D")
    skill.save()
    collaborator_skill_relation = CollaboratorSkill(main_skill="True",
                                                    collaborator=collaborator,
                                                    skill=skill)
    collaborator_skill_relation.save()

    return collaborator

def create_collaborator2_compositing_for_test():
    collaborator = Collaborator(name="Second collaborator",
                                email="email",
                                phone="5555555556",
                                position="Rome",
                                availability="Always")
    collaborator.save()
    skill = Skill(skill="Compositing")
    skill.save()
    collaborator_skill_relation = CollaboratorSkill(main_skill="True",
                                                    collaborator=collaborator,
                                                    skill=skill)
    collaborator_skill_relation.save()

    return collaborator

def create_skill_compositing_for_test():
    skill = Skill(skill="Compositing")
    skill.save()
    return skill

def create_skill_3D_for_test():
    skill = Skill(skill="3D")
    skill.save()
    return skill
