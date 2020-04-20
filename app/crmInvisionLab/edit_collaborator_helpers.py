from .models import CollaboratorSkill, Skill


def edit_relation_skill_table(collaborator, skill):
    relation_skills = CollaboratorSkill.objects.get(collaborator=collaborator.id)
    new_skill = Skill.objects.get(skill=skill)
    relation_skills.skill = new_skill
    relation_skills.save()
