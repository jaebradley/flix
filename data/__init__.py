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

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


class Performance:
    def __init__(self, start_time, code):
        self.start_time = start_time
        self.code = code

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


class PresentationCategory(Enum):
    STANDARD = "STANDARD"
    THREE_D = "THREE_D"
    IMAX = "IMAX"
    FOUR_K = "FOUR_K"
    THREE_D_4K = "THREE_D_4K"
    IMAX_3D = "IMAX_3D"
    IMAX_3D_4K = "IMAX_3D_4K"
    IMAX_4K = "IMAX_4K"

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

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


class MovieSchedule:
    def __init__(self, movie_id, presentations):
        self.movie_id = movie_id
        self.presentations = presentations

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


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

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


class Actor:
    def __init__(self, fid, name, url):
        self.fid = fid
        self.name = name
        self.url = url

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


class FlixsterMovieDetails:
    def __init__(self, average_rating, not_interested_count, likability_score, scores_count, want_to_see_count, popcorn_score):
        self.average_rating = average_rating
        self.not_interested_count = not_interested_count
        self.likability_score = likability_score
        self.scores_count = scores_count
        self.want_to_see_count = want_to_see_count
        self.popcorn_score = popcorn_score

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


class RottenTomatoesMovieDetails:
    def __init__(self, rating, is_certified_fresh, consensus):
        self.rating = rating
        self.is_certified_fresh = is_certified_fresh
        self.consensus = consensus

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


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
        self.flixster_movie_details = flixster_movie_details
        self.rotten_tomatoes_movie_details = rotten_tomatoes_movie_details

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


class MoviePresentations:
    def __init__(self, date, theaters, movie_presentations_mapping):
        self.date = date
        self.theaters = theaters
        self.movie_presentations_mapping = movie_presentations_mapping

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))
