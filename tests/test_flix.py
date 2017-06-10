from unittest import TestCase

from data.services import fetch_parsed_theater_data
from tables.builders import build_table


class TestFlix(TestCase):
    def test_should_create_table(self):
        movie_presentations = fetch_parsed_theater_data()
        build_table(movie_presentations)
