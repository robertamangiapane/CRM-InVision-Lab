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
        self.assertIn(collaborator2.name, response_text)

    def test_user_add_collaborator(self):
        create_skill_compositing_for_test()
        self.client.post('/add/', {'name': "Added collaborator",
                                   'email': "email",
                                   'phone': "5555555555",
                                   'position': "Rome",
                                   'availability': "Weekend",
                                   'main_skill': "Compositing"})

        response = self.client.get('/')
        response_text = response.content.decode("utf-8")

        self.assertIn("Added collaborator", response_text)


    def test_added_collaborator_redirect_to_home(self):
        create_skill_compositing_for_test()

        response = self.client.post('/add/', {'name': "Added collaborator",
                                              'email': "email",
                                              'phone': "5555555555",
                                              'position': "Rome",
                                              'availability': "Weekend",
                                              'main_skill': "Compositing"})

        self.assertRedirects(response, '/')

    def test_user_cannot_add_collaborator_without_name(self):
        create_skill_compositing_for_test()

        with self.assertRaises(ValidationError):
            self.client.post('/add/', {'name': "",
                                       'email': "email",
                                       'phone': "5555555555",
                                       'position': "Rome",
                                       'availability': "Weekend",
                                       'main_skill': "Compositing"})

    def test_view_collaborator_page(self):
        create_skill_compositing_for_test()

        self.client.post('/add/', {'name': "Added collaborator",
                                   'email': "email",
                                   'phone': "5555555555",
                                   'position': "Rome",
                                   'availability': "Weekend",
                                   'main_skill': "Compositing"})

        collaborator = Collaborator.objects.get(name="Added collaborator")
        response = self.client.get('/collaborator/' + str(collaborator.id))

        response_text = response.content.decode("utf-8")

        self.assertIn("Added collaborator", response_text)

    def test_edit_collaborator_skill_relationship_table(self):
        collaborator = create_collaborator1_3D_for_test()
        create_skill_compositing_for_test()

        self.client.post('/edit/' + str(collaborator.id), {'name': "Collaborator edited",
                                                           'email': "email",
                                                           'phone': "5555555555",
                                                           'position': "Rome",
                                                           'availability': "Weekend",
                                                           'main_skill': "Compositing"})

        response = self.client.get('/collaborator/' + str(collaborator.id))

        response_text = response.content.decode("utf-8")
        self.assertIn("Compositing", response_text)
