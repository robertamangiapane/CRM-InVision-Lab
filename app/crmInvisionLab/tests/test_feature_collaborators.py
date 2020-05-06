from django.test import Client
from django.test import TestCase
from .helpers import *


class FeatureTestInfrastructure(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage_displays_all_collaborators(self):
        collaborator1 = create_collaborator1_skill1_for_test()
        collaborator2 = create_collaborator2_skill2_for_test()

        response = self.client.get('/collaborators')
        response_text = response.content.decode("utf-8")

        self.assertIn(collaborator1.name, response_text)
        self.assertIn("skill one", response_text)

        self.assertIn(collaborator2.name, response_text)
        self.assertIn("skill two", response_text)

    def test_user_add_collaborator(self):
        skill = create_skill2_for_test()
        response = self.client.post('/collaborators/add/collaborator',
                                    {'name': "Added collaborator",
                                     'email': "test@test.com",
                                     'phone': "05555555555",
                                     'position': "Position",
                                     'availability': "Availability",
                                     'main_skills': skill.id})

        collaborator = Collaborator.objects.get(name="Added collaborator")
        self.assertRedirects(response, '/collaborators/view/' + str(collaborator.id))

        response = self.client.get('/collaborators')
        response_text = response.content.decode("utf-8")

        self.assertIn("Added collaborator", response_text)

    def test_added_collaborator_with_multiple_skills(self):
        skill1 = create_skill2_for_test()
        skill2 = create_skill1_for_test()

        response = self.client.post('/collaborators/add/collaborator',
                                    {'name': "Added collaborator",
                                     'email': "test@test.com",
                                     'phone': "05555555555",
                                     'position': "Position",
                                     'availability': "Availability",
                                     'main_skills': [skill1.id, skill2.id]})

        collaborator = Collaborator.objects.get(name="Added collaborator")
        self.assertRedirects(response, '/collaborators/view/' + str(collaborator.id))

        response = self.client.get('/collaborators/view/' + str(collaborator.id))
        response_text = response.content.decode("utf-8")

        self.assertIn("skill two", response_text)
        self.assertIn("skill one", response_text)

    def test_user_can_edit_a_collaborator(self):
        collaborator = create_collaborator1_skill1_for_test()
        skill2 = Skill.objects.get(name="skill one")
        skill = create_skill2_for_test()

        self.client.post('/collaborators/edit/' + str(collaborator.id),
                         {'name': "Collaborator edited",
                          'email': "test@test.com",
                          'phone': "05555555555",
                          'position': "Position",
                          'availability': "Availability",
                          'main_skills': [skill.id, skill2.id]})

        response = self.client.get('/collaborators/view/' + str(collaborator.id))

        response_text = response.content.decode("utf-8")
        self.assertIn("skill two", response_text)
        self.assertIn("skill one", response_text)

    def test_user_can_delete_a_collaborator(self):
        collaborator = create_collaborator1_skill1_for_test()
        self.client.post('/collaborators/delete/' + str(collaborator.id))
        response = self.client.get('/collaborators')
        response_text = response.content.decode("utf-8")

        self.assertNotIn("First collaborator", response_text)

    def test_user_can_search_collaborator_with_one_filters(self):
        create_collaborator1_skill1_for_test()
        create_collaborator2_skill2_for_test()
        response = self.client.get('/collaborators', {
            'name': "",
            'email': "",
            'phone': "",
            'position': "Position",
            'availability': "",
            'main_skills': "",
            'secondary_skills': "",
            'search': "OK"})

        response_text = response.content.decode("utf-8")

        self.assertIn("First collaborator", response_text)
        self.assertNotIn("Second collaborator", response_text)

    # def test_user_can_search_collaborator_with_more_filters(self):
    #     create_collaborator3_with_main_and_secondary_skills_for_test()
    #     create_collaborator2_skill2_for_test()
    #     response = self.client.get('/collaborators', {
    #         'name': "",
    #         'email': "",
    #         'phone': "",
    #         'position': "Position",
    #         'availability': "",
    #         'main_skills': "skill one",
    #         'secondary_skills': "Secondary",
    #         'search': "OK"})
    # 
    #     response_text = response.content.decode("utf-8")
    # 
    #     self.assertIn("Third collaborator", response_text)
    #     self.assertNotIn("Second collaborator", response_text)





