import re

import dateutil

from data import Actor, FlixsterMovieDetails, RottenTomatoesMovieDetails, Movie


def parse_rotten_tomatoes_movie_details(movie_details):
    return RottenTomatoesMovieDetails(rating=movie_details["rating"],
                                      is_certified_fresh=movie_details["certifiedFresh"],
                                      consensus=clean_html(movie_details["consensus"]))


def parse_movie(movie_details):
    return Movie(fid=movie_details["id"],
                 release_date=parse_release_date(movie_details["releaseDate"]),
                 title=movie_details["title"],
                 mpaa_rating=movie_details["mpaa"],
                 run_time=movie_details["runningTime"],
                 is_live=movie_details["isLive"],
                 is_opening=movie_details["isOpening"],
                 trailer_url=parse_trailer_url(movie_details["trailer"]),
                 actors=parse_actors(movie_details["actors"]),
                 flixster_movie_details=get_flixster_movie_details(movie_details["reviews"]),
                 rotten_tomatoes_movie_details=get_rotten_tomatoes_movie_details(movie_details["reviews"]))


def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    clean_text = re.sub(cleanr, '', raw_html)
    return clean_text


def parse_actor(actor_details):
    return Actor(fid=actor_details["id"], name=actor_details["name"], url=actor_details["url"])


def parse_flixster_movie_details(movie_details):
    return FlixsterMovieDetails(average_rating=movie_details["average"],
                                not_interested_count=movie_details["numNotInterested"],
                                likability_score=movie_details["likeability"],
                                scores_count=movie_details["numScores"],
                                want_to_see_count=movie_details["numWantToSee"],
                                popcorn_score=movie_details["popcornScore"])


def parse_trailer_url(trailer_details):
    if "hd" in trailer_details:
        return trailer_details["hd"]

    return None


def parse_release_date(release_date):
    if release_date != "":
        return dateutil.parser.parse(release_date)

    return None


def parse_actors(actors):
    return [parse_actor(actor) for actor in actors]


def get_rotten_tomatoes_movie_details(reviews):
    if "rottenTomatoes" in reviews:
        return parse_rotten_tomatoes_movie_details(reviews["rottenTomatoes"])

    return None


def get_flixster_movie_details(reviews):
    if "flixster" in reviews:
        return parse_flixster_movie_details(reviews["flixster"])

    return None
