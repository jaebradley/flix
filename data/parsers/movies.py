from data import Actor, FlixsterMovieDetails, RottenTomatoesMovieDetails, Movie

import dateutil


import re


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
                                scores_count=movie_details["numScores"], want_to_see_count=movie_details["numWantToSee"],
                                popcorn_score=movie_details["popcornScore"])


def parse_rotten_tomatoes_movie_details(movie_details):
    return RottenTomatoesMovieDetails(rating=movie_details["rating"], is_certified_fresh=movie_details["certifiedFresh"], consensus=clean_html(movie_details["consensus"]))


def parse_movie(movie_details):
    actors = [
        parse_actor(actor)
        for actor in movie_details["actors"]
    ]
    reviews = movie_details["reviews"]
    flixster_movie_details = parse_flixster_movie_details(reviews["flixster"]) if "flixster" in movie_details["reviews"] else None
    rotten_tomatoes_movie_details = parse_rotten_tomatoes_movie_details(reviews["rottenTomatoes"]) if "rottenTomatoes" in movie_details["reviews"] else None
    return Movie(fid=movie_details["id"],
                 release_date=dateutil.parser.parse(movie_details["releaseDate"]) if movie_details["releaseDate"] != "" else None,
                 title=movie_details["title"],
                 mpaa_rating=movie_details["mpaa"],
                 run_time=movie_details["runningTime"],
                 is_live=movie_details["isLive"],
                 is_opening=movie_details["isOpening"],
                 trailer_url=movie_details["trailer"]["hd"] if "hd" in movie_details["trailer"] else None,
                 actors=actors,
                 flixster_movie_details=flixster_movie_details,
                 rotten_tomatoes_movie_details=rotten_tomatoes_movie_details)
