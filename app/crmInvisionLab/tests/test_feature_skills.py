from django.test import Client
from django.test import TestCase
from .helpers import *


class FeatureTestInfrastructure(TestCase):
    def setUp(self):
        self.client = Client()

    def test_display_skills_homepage(self):
        create_skill_3D_for_test()
        create_skill_compositing_for_test()

        response = self.client.get('/skills')
        response_text = response.content.decode("utf-8")

        self.assertIn("Compositing", response_text)
        self.assertIn("3D", response_text)

    def test_user_can_add_a_skill(self):
        self.client.post('/skills/add', {'skill': "3D"})
        response = self.client.get('/skills')
        response_text = response.content.decode("utf-8")

        self.assertIn("3D", response_text)

    def test_user_can_delete_skill(self):
        skill1 = create_skill_3D_for_test()

        self.client.post('/skills/delete/' + str(skill1.id))
        response = self.client.get('/skills')
        response_text = response.content.decode("utf-8")

        self.assertNotIn("3D", response_text)

    def test_user_can_edit_skill(self):
        skill1 = create_wrong_skill_for_test()
        self.client.post('/skills/edit/' + str(skill1.id), {skill1.name: "Right"})
        response = self.client.get('/skills')
        response_text = response.content.decode("utf-8")

        self.assertNotIn("Wrong", response_text)
        self.assertIn("Right", response_text)



