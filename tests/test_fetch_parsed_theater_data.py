from unittest import TestCase

from data.services import fetch_parsed_theater_data


class TestFetch_parsed_theater_data(TestCase):
    def test_fetch(self):
        fetch_parsed_theater_data()
