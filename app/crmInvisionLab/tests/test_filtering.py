from django.test import TestCase
from ..collaborators.collaborators_filtering_helpers import *
from ..models import Skill


class FilteringTest(TestCase):
    def setUp(self):
        self.skill1 = Skill(name="skill one")
        self.skill2 = Skill(name="skill two")
        self.filters = {
            'name': '',
            'email': '',
            'phone': '',
            'position': 'test position',
            'availability': 'test availability',
            'main_skills': self.skill1,
            'secondary_skills': self.skill2}

    def test_get_real_filter(self):
        result = {
            'position': "test position",
            'availability': "test availability",
            'main_skills': self.skill1,
            'secondary_skills': self.skill2}

        real_filter = get_real_filter(self.filters)

        self.assertEqual(result, real_filter)

    def test_getting_columns_dict(self):
        real_filters = get_real_filter(self.filters)
        result = {
            'position__exact': "test position",
            'availability__exact': "test availability"}
        columns = get_columns_dict(real_filters)

        self.assertEqual(result, columns)

    def test_get_m_to_m_dict(self):
        real_filters = get_real_filter(self.filters)
        result = {'main_skills__name__contains': "skill one", 'secondary_skills__name__contains': "skill two"}
        m_to_m_dict = get_m_to_m_dict(real_filters)

        self.assertEqual(result, m_to_m_dict)

