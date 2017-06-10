from datetime import date

from flixster import FlixsterClient, TheaterInformationQuery

from data import MoviePresentations
from data.parsers.movies import parse_movie
from data.parsers.theaters import parse_theater


def fetch_parsed_theater_data(start_date=date.today(), movie_name=None, limit=2):
    query = TheaterInformationQuery(date=start_date, limit=limit)
    theaters_response = FlixsterClient.get_theater_information(query)
    theaters = [parse_theater(theater) for theater_id, theater in theaters_response["theaters"].items()]
    if movie_name is not None:
        movies = [parse_movie(movie) for movie in theaters_response["movies"].values() if movie_name.lower() in movie["title"].lower()]
    else:
        movies = [parse_movie(movie)for movie_id, movie in theaters_response["movies"].items()]

    return build_movie_presentations(date=start_date, movies=movies, theaters=theaters)


def build_movie_presentations(date, movies, theaters):
    movie_presentations_mapping = {}

    for movie in movies:
        movie_presentations_mapping[movie.fid] = {"theaters": {}}
        movie_presentations_mapping[movie.fid]["details"] = movie
        for theater in theaters:
            movie_presentations_mapping[movie.fid]["theaters"][theater.fid] = {"show_times": {}}
            movie_presentations_mapping[movie.fid]["theaters"][theater.fid]["details"] = theater
            for movie_schedule in theater.movie_schedules:
                if movie_schedule.movie_id == movie.fid:
                    movie_presentations_mapping[movie.fid]["theaters"][theater.fid] = {"category": {}}
                    for presentation in movie_schedule.presentations:
                        category = movie_presentations_mapping[movie.fid]["theaters"][theater.fid]["category"]
                        category[presentation.category] = [performance.start_time for performance in
                                                           presentation.performances]

    return MoviePresentations(date=date, theaters=theaters, movie_presentations_mapping=movie_presentations_mapping)
