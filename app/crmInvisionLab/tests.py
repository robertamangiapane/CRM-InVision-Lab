from django.core.exceptions import ValidationError
from django.test import Client
from django.test import TestCase
from .models import Collaborator
from django import forms


class FeatureTestInfrastructure(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage_displays_all_collaborators(self):
        collaborator1 = Collaborator("1", "First collaborator", "email", "5555555555", "Rome", "Weekend", "One skill",
                                     "Two skill")
        collaborator2 = Collaborator("2", "Second collaborator", "email", "5555555556", "Rome", "Always", "One skill",
                                     "Two skill")

        collaborator1.save()
        collaborator2.save()

        response = self.client.get('/')
        response_text = response.content.decode("utf-8")

        self.assertIn(collaborator1.name, response_text)
        self.assertIn(collaborator2.name, response_text)

    def test_user_add_collaborator(self):
        self.client.post('/add/', {'name': "Added collaborator", 'email': "email", 'phone': "5555555555",
                                   'position': "Rome", 'availability': "Weekend",
                                   'main_skills': "One skill", 'secondary_skills': "Two skill"})

        response = self.client.get('/')
        response_text = response.content.decode("utf-8")

        self.assertIn("Added collaborator", response_text)

    def test_added_collaborator_redirect_to_home(self):
        response = self.client.post('/add/', {'name': "Added collaborator", 'email': "email", 'phone': "5555555555",
                                              'position': "Rome", 'availability': "Weekend",
                                              'main_skills': "One skill",
                                              'secondary_skills': "Two skill"})

        self.assertRedirects(response, '/')

    def test_user_cannot_add_collaborator_without_name(self):
        with self.assertRaises(ValidationError):
            self.client.post('/add/', {'name': "", 'email': "email", 'phone': "5555555555",
                                       'position': "Rome", 'availability': "Weekend",
                                       'main_skills': "One skill",
                                       'secondary_skills': "Two skill"})

    def test_view_collaborator_page(self):
        self.client.post('/add/', {'name': "Added collaborator", 'email': "email", 'phone': "5555555555",
                                   'position': "Rome", 'availability': "Weekend",
                                   'main_skills': "One skill", 'secondary_skills': "Two skill"})
        collaborator = Collaborator.objects.get(name="Added collaborator")
        collaborator_page = self.client.get('/collaborator/' + str(collaborator.id))

        response_text = collaborator_page.content.decode("utf-8")

        self.assertIn("Added collaborator", response_text)


    def test_edit_collaborators(self):
        response = self.client.get('/edit/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Edit a selected collaborator")

    # def test_user_input_wrong_date_format(self):
    # string or wrong date
