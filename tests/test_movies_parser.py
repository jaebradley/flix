from unittest import TestCase

from mock import Mock, patch
from data.parsers.movies import get_flixster_movie_details, get_rotten_tomatoes_movie_details, get_actors, \
    get_release_date


class TestGetFlixsterDetails(TestCase):
    def test_returns_none_for_missing_details(self):
        self.assertIsNone(get_flixster_movie_details({}))

    @patch("data.parsers.movies.parse_flixster_movie_details")
    def test_returns_parsed_flixster_movie_details(self, mocked_details_parser):
        details = "details"
        mocked_details_parser.return_value = details
        self.assertEqual(details, get_flixster_movie_details({"flixster": "foo"}))


class TestGetRottenTomatoesMovieDetails(TestCase):
    def test_returns_none_for_missing_details(self):
        self.assertIsNone(get_rotten_tomatoes_movie_details({}))

    @patch("data.parsers.movies.parse_rotten_tomatoes_movie_details")
    def test_returns_parsed_rotten_tomatoes_movie_details(self, mocked_details_parser):
        details = "details"
        mocked_details_parser.return_value = details
        self.assertEqual(details, get_rotten_tomatoes_movie_details({"rottenTomatoes": "foo"}))


class TestGetReleaseDate(TestCase):
    def test_returns_none_for_empty_release_date(self):
        self.assertIsNone(get_release_date(""))

    @patch("dateutil.parser.parse")
    def test_returns_parsed_date(self, mocked_date_parser):
        parsed_date = "parsed date"
        mocked_date_parser.return_value = parsed_date
        self.assertEqual(parsed_date, get_release_date("foo"))


class TestGetActors(TestCase):
    @patch("data.parsers.movies.parse_actor")
    def test_returns_actors(self, mocked_actors_parser):
        parsed_actor = "parsed actor"
        mocked_actors_parser.return_value = parsed_actor
        expected = [parsed_actor, parsed_actor]
        self.assertEqual(expected, get_actors([1, 2]))