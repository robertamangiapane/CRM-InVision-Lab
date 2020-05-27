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

        client = Customer.objects.get(name="First client")
        self.assertRedirects(response, '/clients/view/' + str(client.id))

        response = self.client_http.get('/clients')
        response_text = response.content.decode("utf-8")

        self.assertIn("First client", response_text)

    def test_user_can_delete_client(self):
        client = create_client1()
        self.client_http.post('/clients/delete/' + str(client.id))

        response = self.client_http.get('/clients')
        response_text = response.content.decode("utf-8")

        self.assertNotIn("First client", response_text)

    def test_user_can_update_a_client(self):
        client = create_client1()

        self.client_http.post('/clients/update/' + str(client.id),
                              {'name': 'New name'})

        response = self.client.get('/clients/view/' + str(client.id))
        response_text = response.content.decode("utf-8")
        self.assertIn("New name", response_text)

    def test_user_can_search_client_with_one_filter(self):
        create_client1()
        create_client2()
        response = self.client_http.get('/clients', {
            'name': "First client",
            'search': "OK"})

        response_text = response.content.decode("utf-8")

        self.assertIn("First client", response_text)
        self.assertNotIn("Second client", response_text)