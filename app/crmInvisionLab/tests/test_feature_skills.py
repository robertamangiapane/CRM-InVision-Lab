from django.test import Client
from django.test import TestCase
from .helpers import *


class FeatureTestInfrastructure(TestCase):
    def setUp(self):
        self.client = Client()

    def test_display_skills_homepage(self):
        create_skill1_for_test()
        create_skill2_for_test()

        response = self.client.get('/skills')
        response_text = response.content.decode("utf-8")

        self.assertIn("skill two", response_text)
        self.assertIn("skill one", response_text)

    def test_user_can_add_a_skill(self):
        self.client.post('/skills', {'name': "skill one"})
        response = self.client.get('/skills')
        response_text = response.content.decode("utf-8")

        self.assertIn("skill one", response_text)

    def test_user_can_delete_skill(self):
        skill1 = create_skill1_for_test()

        self.client.post('/skills/delete/' + str(skill1.id))
        response = self.client.get('/skills')
        response_text = response.content.decode("utf-8")

        self.assertNotIn("3D", response_text)

    def test_user_can_edit_skill(self):
        skill1 = create_wrong_skill_for_test()

        self.client.post('/skills/update/' + str(skill1.id), {"name": "Right"})
        response = self.client.get('/skills')
        response_text = response.content.decode("utf-8")

        self.assertNotIn("Wrong", response_text)
        self.assertIn("Right", response_text)



