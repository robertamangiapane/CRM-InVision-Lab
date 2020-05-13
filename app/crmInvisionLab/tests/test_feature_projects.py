from django.test import Client
from django.test import TestCase
from .helpers import *
from ..models import Job


class FeatureTestProject(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_can_add_new_project(self):
        # collaborator1 = create_collaborator1_skill1_for_test()
        # collaborator2 = create_collaborator2_skill2_for_test()
        response = self.client.post('/projects/add/project',
                                    {'name': 'First project'})
        project = Job.objects.get(name='First project')
        self.assertRedirects(response, '/projects/view/' + str(project.id))

        response = self.client.get('/projects/view/' + str(project.id))
        response_text = response.content.decode("utf-8")

        self.assertIn("First project", response_text)
        # self.assertIn("First collaborator", response_text)
        # self.assertIn("Second collaborator", response_text)

