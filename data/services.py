from flixster import FlixsterClient, TheaterInformationQuery

from data import TheatersData
from data.parsers.movies import parse_movie
from data.parsers.theaters import parse_theater


def fetch_parsed_theater_data(date, movie_id=None, limit=5):
    query = TheaterInformationQuery(date=date, movie_id=movie_id, limit=limit)
    theaters_response = FlixsterClient.get_theater_information(query)
    theaters = [
        parse_theater(theater)
        for theater in theaters_response["theaters"]
    ]
    movies = [
        parse_movie(movie)
        for movie in theaters_response["movies"]
    ]
    return TheatersData(theaters=theaters, movies=movies)
