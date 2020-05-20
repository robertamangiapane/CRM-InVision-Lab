from django.test import Client
from django.test import TestCase
from .helpers import *
from ..models import Job


class FeatureTestClient(TestCase):
    def setUp(self):
        self.client_http = Client()

    def test_my_clients_page_display_all_clients(self):
        create_client1()
        create_client2()
        response = self.client_http.get('/clients')
        response_text = response.content.decode("utf-8")

        self.assertIn("First client", response_text)
        self.assertIn("Second client", response_text)

    # def test_my_ongoing_projects_display_only_not_finished_projects(self):
    #     create_finished_project()
    #     create_not_finished_project()
    #
    #     response = self.client_http.get('/projects/ongoing')
    #     response_text = response.content.decode("utf-8")
    #
    #     self.assertNotIn("Finished", response_text)
    #     self.assertIn("Not finished", response_text)
    #
    # def test_my_old_projects_display_only_finished_projects(self):
    #     create_finished_project()
    #     create_not_finished_project()
    #
    #     response = self.client_http.get('/projects/old')
    #     response_text = response.content.decode("utf-8")
    #
    #     self.assertIn("Finished", response_text)
    #     self.assertNotIn("Not finished", response_text)
    #
    # def test_user_can_add_new_project(self):
    #     collaborator1 = create_collaborator1_skill1_for_test()
    #     collaborator2 = create_collaborator2_skill2_for_test()
    #     response = self.client_http.post('/projects/add/project',
    #                                 {'name': 'First project',
    #                                  'collaborators': [collaborator1.id, collaborator2.id]})
    #     project = Job.objects.get(name='First project')
    #     self.assertRedirects(response, '/projects/view/' + str(project.id))
    #
    #     response = self.client_http.get('/projects/view/' + str(project.id))
    #     response_text = response.content.decode("utf-8")
    #
    #     self.assertIn("First project", response_text)
    #
    # def test_user_can_delete_project(self):
    #     project = create_finished_project()
    #     self.client_http.post('/projects/delete/' + str(project.id))
    #
    #     response = self.client_http.get('/projects')
    #     response_text = response.content.decode("utf-8")
    #
    #     self.assertNotIn("Finished", response_text)
    #
    # def test_user_can_update_a_project(self):
    #     project = create_not_finished_project()
    #
    #     self.client_http.post('/projects/update/' + str(project.id),
    #                      {'name': 'Project finished'})
    #
    #     response = self.client.get('/projects/view/' + str(project.id))
    #     response_text = response.content.decode("utf-8")
    #     self.assertIn("Project finished", response_text)
    #
    # def test_user_can_search_project_with_one_filter(self):
    #     create_not_finished_project()
    #     create_finished_project()
    #     response = self.client_http.get('/projects', {
    #         'name': "Finished",
    #         'search': "OK"})
    #
    #     response_text = response.content.decode("utf-8")
    #
    #     self.assertIn("Finished", response_text)
    #     self.assertNotIn("Not finished", response_text)