from django.core.exceptions import ValidationError
from django.test import Client
from django.test import TestCase
from .models import Collaborator
from .models import Skill
from .tests_helpers import *


class FeatureTestInfrastructure(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage_displays_all_collaborators(self):
        collaborator1 = create_collaborator1_for_test()
        collaborator2 = create_collaborator2_for_test()

        response = self.client.get('/')
        response_text = response.content.decode("utf-8")

        self.assertIn(collaborator1.name, response_text)
        self.assertIn(collaborator2.name, response_text)

    def test_user_add_collaborator(self):
        create_skill1_for_test()
        self.client.post('/add/', {'name': "Added collaborator", 'email': "email", 'phone': "5555555555",
                                   'position': "Rome", 'availability': "Weekend",
                                   'main_skill': "Compositing"})

        response = self.client.get('/')
        response_text = response.content.decode("utf-8")

        self.assertIn("Added collaborator", response_text)


    def test_added_collaborator_redirect_to_home(self):
        create_skill1_for_test()

        response = self.client.post('/add/', {'name': "Added collaborator", 'email': "email", 'phone': "5555555555",
                                              'position': "Rome", 'availability': "Weekend", 'main_skill': "Compositing"})

        self.assertRedirects(response, '/')

    def test_user_cannot_add_collaborator_without_name(self):
        create_skill1_for_test()

        with self.assertRaises(ValidationError):
            self.client.post('/add/', {'name': "", 'email': "email", 'phone': "5555555555",
                                       'position': "Rome", 'availability': "Weekend",
                                       'main_skill': "Compositing"})

    def test_view_collaborator_page(self):
        create_skill1_for_test()

        self.client.post('/add/', {'name': "Added collaborator", 'email': "email", 'phone': "5555555555",
                                   'position': "Rome", 'availability': "Weekend",
                                   'main_skill': "Compositing"})
        collaborator = Collaborator.objects.get(name="Added collaborator")
        collaborator_page = self.client.get('/collaborator/' + str(collaborator.id))

        response_text = collaborator_page.content.decode("utf-8")

        self.assertIn("Added collaborator", response_text)

    def test_edit_collaborator_page_shows_edit_form(self):
        collaborator = create_collaborator1_for_test()
        response = self.client.get('/edit/' + str(collaborator.id))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Edit a selected collaborator")

    def test_edit_collaborator_redirect_edited_collaborator_page(self):
        create_collaborator1_for_test()
        create_skill1_for_test()
        create_skill2_for_test()

        collaborator_edited = self.client.post('/edit/1', {'name': "Collaborator edited", 'email': "email", 'phone': "5555555555",
                                   'position': "Rome", 'availability': "Weekend",
                                   'main_skill': "Compositing"})

        response_text = collaborator_edited.content.decode("utf-8")

        self.assertIn("Collaborator edited", response_text)


        # collaborator = Collaborator("1", "First collaborator", "email", "5555555555", "Rome", "Weekend")
        # collaborator.save()
        # skill1 = Skill("1", "3D")
        # skill1.save()
        # skill2 = Skill("1", "3D")
        # skill2.save()
        #
        # response = self.client.get('/edit/' + str(collaborator.id))
        # self.client.post('/edit/', {'name': "Added collaborator", 'email': "email", 'phone': "5555555555",
        #                            'position': "Rome", 'availability': "Weekend",
        #                            'main_skill': "Compositing"})

        # self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.content, b"Edit a selected collaborator")

