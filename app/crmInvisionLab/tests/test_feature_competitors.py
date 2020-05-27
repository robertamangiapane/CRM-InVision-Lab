from django.test import Client
from django.test import TestCase
from .helpers import *
from ..models import Competitor


class FeatureTestCompetitor(TestCase):
    def setUp(self):
        self.client = Client()

    def test_my_competitors_page_display_all_competitors(self):
        create_competitor1()
        create_competitor2()
        response = self.client.get('/competitors')
        response_text = response.content.decode("utf-8")

        self.assertIn("First competitor", response_text)
        self.assertIn("Second competitor", response_text)

    def test_user_can_add_new_competitor(self):
        response = self.client.post('/competitors/add/competitor',
                                         {'name': 'First competitor'})

        competitor = Competitor.objects.get(name="First competitor")
        self.assertRedirects(response, '/competitors/view/' + str(competitor.id))

        response = self.client.get('/competitors')
        response_text = response.content.decode("utf-8")

        self.assertIn("First competitor", response_text)

    def test_user_can_delete_competitor(self):
        competitor = create_competitor1()
        self.client.post('/competitors/delete/' + str(competitor.id))

        response = self.client.get('/competitors')
        response_text = response.content.decode("utf-8")

        self.assertNotIn("First competitor", response_text)

    def test_user_can_update_a_competitor(self):
        competitor = create_competitor1()

        self.client.post('/competitors/update/' + str(competitor.id),
                              {'name': 'New name'})

        response = self.client.get('/competitors/view/' + str(competitor.id))
        response_text = response.content.decode("utf-8")
        self.assertIn("New name", response_text)

    def test_user_can_search_competitor_with_one_filter(self):
        create_competitor1()
        create_competitor2()
        response = self.client.get('/competitors', {
            'name': "First competitor",
            'search': "OK"})

        response_text = response.content.decode("utf-8")

        self.assertIn("First competitor", response_text)
        self.assertNotIn("Second competitor", response_text)
