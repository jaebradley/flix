from unittest import TestCase

from mock import Mock, patch
from data import FlixsterMovieDetails, Actor, RottenTomatoesMovieDetails, Movie
from data.parsers.movies import get_flixster_movie_details, get_rotten_tomatoes_movie_details, get_actors, \
    get_release_date, get_trailer_url, parse_flixster_movie_details, parse_actor, parse_rotten_tomatoes_movie_details, \
    parse_movie


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


class TestGetTrailerUrl(TestCase):
    def test_returns_none_for_empty_hd_trailer(self):
        self.assertIsNone(get_trailer_url({}))

    def test_returns_hd_trailer(self):
        self.assertEqual("foo", get_trailer_url({"hd": "foo"}))


class TestParseFlixsterMovieDetails(TestCase):
    average = "average"
    not_interested_count = "not interested count"
    likability_score = "likability score"
    scores_count = "scores count"
    want_to_see_count = "want to see count"
    popcorn_score = "popcorn score"
    movie_details = {
        "average": average,
        "numNotInterested": not_interested_count,
        "likeability": likability_score,
        "numScores": scores_count,
        "numWantToSee": want_to_see_count,
        "popcornScore": popcorn_score
    }
    expected = FlixsterMovieDetails(average_rating=average, not_interested_count=not_interested_count,
                                    likability_score=likability_score, scores_count=scores_count,
                                    want_to_see_count=want_to_see_count, popcorn_score=popcorn_score)

    def test_parses_successfully(self):
        self.assertEqual(self.expected, parse_flixster_movie_details(self.movie_details))


class TestParseActor(TestCase):
    id = "id"
    name = "name"
    url = "url"
    actor_details = {
        "id": id,
        "name": name,
        "url": url
    }
    expected = Actor(fid=id, name=name, url=url)

    def test_parses_successfully(self):
        self.assertEqual(self.expected, parse_actor(self.actor_details))


class TestParseRottenTomatoesMovieDetails(TestCase):
    rating = "rating"
    is_certified_fresh = "certified fresh"
    consensus = "consensus"
    movie_details = {
        "rating": rating,
        "certifiedFresh": is_certified_fresh,
        "consensus": consensus
    }
    expected = RottenTomatoesMovieDetails(rating=rating, is_certified_fresh=is_certified_fresh, consensus=consensus)

    @patch("data.parsers.movies.clean_html")
    def test_parses_successfully(self, mocked_html_cleaner):
        mocked_html_cleaner.return_value = self.consensus
        self.assertEqual(self.expected, parse_rotten_tomatoes_movie_details(self.movie_details))


class TestParseMovie(TestCase):
    id = "id"
    release_date = "release date"
    title = "title"
    mpaa_rating = "mpaa rating"
    run_time = "run time"
    is_live = "is live"
    is_opening = "is opening"
    trailer_url = "trailer url"
    actors = "actors"
    flixster_movie_details = "flixster movie details"
    rotten_tomatoes_movie_details = "rotten tomatoes movie details"
    reviews = "reviews"

    movie_details = {
        "id": id,
        "releaseDate": release_date,
        "title": title,
        "mpaa": mpaa_rating,
        "runningTime": run_time,
        "isLive": is_live,
        "isOpening": is_opening,
        "trailer": trailer_url,
        "actors": actors,
        "reviews": reviews
    }

    @patch("data.parsers.movies.get_release_date")
    @patch("data.parsers.movies.get_trailer_url")
    @patch("data.parsers.movies.get_actors")
    @patch("data.parsers.movies.get_flixster_movie_details")
    @patch("data.parsers.movies.get_rotten_tomatoes_movie_details")
    def test_parses_successfully(self, mocked_rotten_tomatoes_movie_details, mocked_flixster_movie_details, mocked_actors, mocked_trailer_url, mocked_release_date):
        rotten_tomatoes_movie_details = "mocked rotten tomatoes movie details"
        flixster_movie_details = "mocked flixster movie details"
        actors = "mocked actors"
        trailer_url = "mocked trailer url"
        release_date = "mocked release date"
        mocked_rotten_tomatoes_movie_details.return_value = rotten_tomatoes_movie_details
        mocked_flixster_movie_details.return_value = flixster_movie_details
        mocked_actors.return_value = actors
        mocked_trailer_url.return_value = trailer_url
        mocked_release_date.return_value = release_date

        expected = Movie(fid=self.id, release_date=release_date, title=self.title, mpaa_rating=self.mpaa_rating,
                         run_time=self.run_time, is_live=self.is_live, is_opening=self.is_opening, trailer_url=trailer_url,
                         actors=actors, flixster_movie_details=flixster_movie_details, rotten_tomatoes_movie_details=rotten_tomatoes_movie_details)

        self.assertEqual(expected, parse_movie(self.movie_details))