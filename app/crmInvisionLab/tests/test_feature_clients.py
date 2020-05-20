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

    def test_user_can_add_new_client(self):
        response = self.client_http.post('/clients/add/client',
                                         {'name': 'First client'})
        # client = Customer.objects.get(name='First client')
        # self.assertRedirects(response, '/clients/view/' + str(client.id))
        #
        # response = self.client_http.get('/clients/view/' + str(client.id))
        response = self.client_http.get('/clients')
        response_text = response.content.decode("utf-8")

        self.assertIn("First client", response_text)

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