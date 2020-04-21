from .models import Skill


def relation_skill_table_helpers(collaborator, skill_name):
    skill = Skill.objects.get(skill=skill_name)
    collaborator.main_skills.add(skill)
    collaborator.save()
