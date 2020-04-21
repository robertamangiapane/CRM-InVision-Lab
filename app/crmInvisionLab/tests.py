from django.core.exceptions import ValidationError
from django.test import Client
from django.test import TestCase
from .tests_helpers import *


class FeatureTestInfrastructure(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage_displays_all_collaborators(self):
        collaborator1 = create_collaborator1_3D_for_test()
        collaborator2 = create_collaborator2_compositing_for_test()

        response = self.client.get('/')
        response_text = response.content.decode("utf-8")

        self.assertIn(collaborator1.name, response_text)
        self.assertIn("3D", response_text)

        self.assertIn(collaborator2.name, response_text)
        self.assertIn("Compositing", response_text)

    def test_user_add_collaborator(self):
        skill = create_skill_compositing_for_test()
        self.client.post('/add/', {'name': "Added collaborator",
                                   'email': "email",
                                   'phone': "5555555555",
                                   'position': "Rome",
                                   'availability': "Weekend",
                                   'main_skills': skill.id})

        response = self.client.get('/')
        response_text = response.content.decode("utf-8")

        self.assertIn("Added collaborator", response_text)

    def test_added_collaborator_redirect_to_view(self):
        skill = create_skill_compositing_for_test()

        response = self.client.post('/add/', {'name': "Added collaborator",
                                              'email': "email",
                                              'phone': "5555555555",
                                              'position': "Rome",
                                              'availability': "Weekend",
                                              'main_skills': skill.id})

        collaborator = Collaborator.objects.get(name="Added collaborator")
        self.assertRedirects(response, '/collaborator/' + str(collaborator.id))

        response = self.client.get('/collaborator/' + str(collaborator.id))
        response_text = response.content.decode("utf-8")

        self.assertIn("Compositing", response_text)

    def test_added_collaborator_with_multiple_skills(self):
        skill1 = create_skill_compositing_for_test()
        skill2 = create_skill_3D_for_test()

        response = self.client.post('/add/', {'name': "Added collaborator",
                                              'email': "email",
                                              'phone': "5555555555",
                                              'position': "Rome",
                                              'availability': "Weekend",
                                              'main_skills': [skill1.id, skill2.id]})

        collaborator = Collaborator.objects.get(name="Added collaborator")
        self.assertRedirects(response, '/collaborator/' + str(collaborator.id))

        response = self.client.get('/collaborator/' + str(collaborator.id))
        response_text = response.content.decode("utf-8")

        self.assertIn("Compositing", response_text)
        self.assertIn("3D", response_text)

    def test_user_cannot_add_collaborator_without_name(self):
        create_skill_compositing_for_test()

        with self.assertRaises(ValidationError):
            self.client.post('/add/', {'name': "",
                                       'email': "email",
                                       'phone': "5555555555",
                                       'position': "Rome",
                                       'availability': "Weekend",
                                       'main_skills': "Compositing"})

    def test_edit_collaborator_skill_relationship_table(self):
        collaborator = create_collaborator1_3D_for_test()
        skill2 = Skill.objects.get(name="3D")
        skill = create_skill_compositing_for_test()

        self.client.post('/edit/' + str(collaborator.id), {'name': "Collaborator edited",
                                                           'email': "email",
                                                           'phone': "5555555555",
                                                           'position': "Rome",
                                                           'availability': "Weekend",
                                                           'main_skills': [skill.id, skill2.id]})

        response = self.client.get('/collaborator/' + str(collaborator.id))

        response_text = response.content.decode("utf-8")
        self.assertIn("Compositing", response_text)
        self.assertIn("3D", response_text)

