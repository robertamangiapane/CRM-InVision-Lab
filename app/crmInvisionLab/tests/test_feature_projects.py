from django.test import Client
from django.test import TestCase
from .helpers import *
from ..models import Job


class FeatureTestProject(TestCase):
    def setUp(self):
        self.client = Client()

    def test_my_ongoing_projects_display_only_not_finished_projects(self):
        create_finished_project()
        create_not_finished_project()

        response = self.client.get('/projects/ongoing')
        response_text = response.content.decode("utf-8")

        self.assertNotIn("Finished", response_text)
        self.assertIn("Not finished", response_text)

    def test_my_old_projects_display_only_finished_projects(self):
        create_finished_project()
        create_not_finished_project()

        response = self.client.get('/projects/old')
        response_text = response.content.decode("utf-8")

        self.assertIn("Finished", response_text)
        self.assertNotIn("Not finished", response_text)

    def test_user_can_add_new_project(self):

        response = self.client.post('/projects/add/project',
                                    {'name': 'First project'})
        project = Job.objects.get(name='First project')
        self.assertRedirects(response, '/projects/view/' + str(project.id))

        response = self.client.get('/projects/view/' + str(project.id))
        response_text = response.content.decode("utf-8")

        self.assertIn("First project", response_text)


