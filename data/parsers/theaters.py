from dateutil import parser

from data import Address, Performance, PresentationCategory, Presentation, MovieSchedule, Theater


def parse_address(address_details):
    return Address(street=address_details["street"],
                   city=address_details["city"],
                   state=address_details["state"],
                   zip=address_details["zip"],
                   longitude=address_details["longitude"],
                   latitude=address_details["latitude"],
                   distance_from_current_location=address_details["distance"])


def parse_presentation(presentation_details):
    # looks like only one trait group?
    return Presentation(category=PresentationCategory.identify(value=presentation_details["name"]),
                        performances=parse_performances( presentation_details["traitGroups"][0]["performances"]))


def parse_performance(performance_details):
    return Performance(start_time=parser.parse(performance_details["isoDate"]), code=performance_details["code"])


def parse_movie_schedule(schedule_details):
    schedules = []
    for schedule_detail in schedule_details:
        presentations = []
        for presentation in schedule_detail["presentations"]:
            presentations.append(parse_presentation(presentation))
        schedules.append(MovieSchedule(movie_id=schedule_detail["id"], presentations=presentations))
    return schedules


def parse_performances(performances):
    return [parse_performance(performance) for performance in performances]


def parse_movies(movies_details):
    return [parse_movie_schedule(movie_schedule) for movie_schedule in movies_details["movies"]]


def parse_theater(theater_details):
    return Theater(fid=theater_details["id"],
                   name=theater_details["name"],
                   has_fees=theater_details["hasFees"],
                   has_tickets=theater_details["tickets"],
                   ticket_source=theater_details["ticketSource"],
                   screen_count=theater_details["screens"],
                   map_uri=theater_details["map"],
                   phone_number=theater_details["callablePhone"],
                   address=parse_address(theater_details["address"]),
                   seating=theater_details["tags"]["seating"],
                   movie_schedules=parse_movie_schedule(theater_details["movies"]))
