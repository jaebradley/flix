from enum import Enum


class ProximityGroup(Enum):
    WITHIN_A_MILE = "LT_MILES_1"
    WITHIN_THREE_MILES = "LT_MILES_3"
    WITHIN_FIVE_MILES = "LT_MILES_5"
    WITHIN_TEN_MILES = "LT_MILES_10"


class Address:
    def __init__(self, street, city, state, zip, longitude, latitude, distance_from_current_location):
        self.street = street
        self.city = city
        self.state = state
        self.zip = zip
        self.longitude = longitude
        self.latitude = latitude
        self.distance_from_current_location = distance_from_current_location


class Performance:
    def __init__(self, start_time, code):
        self.start_time = start_time
        self.code = code


class PresentationCategory(Enum):
    STANDARD = "Standard"
    THREE_D = "3D"
    IMAX = "IMAX"
    FOUR_K = "4K Digital"
    THREE_D_4K = "3D 4K Digital"
    IMAX_3D = "IMAX 3D"
    IMAX_3D_4K = "IMAX 3D 4K Digital"
    IMAX_4K = "IMAX 4K Digital"

    @staticmethod
    def identify(value):
        for category in PresentationCategory:
            if category.value == value:
                return category

        raise LookupError("Could not identify value: {value}".format(value=value))


class Presentation:
    def __init__(self, category, performances):
        self.category = category
        self.performances = performances


class MovieSchedule:
    def __init__(self, movie_id, presentations):
        self.movie_id = movie_id
        self.presentations = presentations


class Theater:
    def __init__(self, fid, name, has_fees, has_tickets, ticket_source, screen_count, map_uri, phone_number, address,
                 seating, movie_schedules):
        self.fid = fid
        self.name = name
        self.has_fees = has_fees
        self.has_tickets = has_tickets
        self.ticket_source = ticket_source
        self.screen_count = screen_count
        self.map_uri = map_uri
        self.phone_number = phone_number
        self.address = address
        self.seating = seating
        self.movie_schedules = movie_schedules


class Actor:
    def __init__(self, fid, name, url):
        self.fid = fid
        self.name = name
        self.url = url


class FlixsterMovieDetails:
    def __init__(self, average, not_interested_count, likability, scores_count, want_to_see_count, popcorn_score):
        self.average = average
        self.not_interested_count = not_interested_count
        self.likability = likability
        self.scores_count = scores_count
        self.want_to_see_count = want_to_see_count
        self.popcorn_score = popcorn_score


class RottenTomatoesMovieDetails:
    def __init__(self, rating, is_certified_fresh, consensus):
        self.rating = rating
        self.is_certified_fresh = is_certified_fresh
        self.consensus = consensus


class Movie:
    def __init__(self, fid, release_date, title, mpaa_rating, run_time, is_live, is_opening, trailer_url, actors, flixster_movie_details, rotten_tomatoes_movie_details):
        self.fid = fid
        self.release_date = release_date
        self.title = title
        self.mpaa_rating = mpaa_rating
        self.run_time = run_time
        self.is_live = is_live
        self.is_opening = is_opening
        self.trailer_url = trailer_url
        self.actors = actors
        self.rotten_tomatoes_movie_details = rotten_tomatoes_movie_details
