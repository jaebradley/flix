from textwrap import wrap

from colored import fg, attr, stylize

from tables.builders import build_category_table
from tables.utilities import get_mpaa_rating_color, get_movie_rating_percentage_color, get_formatted_boolean


def build_row(movie_presentations):
    row = [get_movie_details_cell(movie_presentations["details"])]
    for theater_id, theater_keys in movie_presentations["theaters"].items():
        if "category" not in theater_keys:
            row.append(stylize("No Times Available", fg("red"), attr("bold")))
        else:
            row.append(build_category_table(theater_keys["category"]))

    return row


def build_theater_metadata_row(theaters):
    return [""] + [get_theater_details_cell(theater) for theater in theaters]


def get_theater_details_cell(theater):
    return """
{phone_number}
{address}
{distance_from_current_location} mi. away

{has_tickets_header} {has_tickets}
{has_fees_header} {has_fees}
    """.format(phone_number=theater.phone_number,
               address=get_formatted_address(theater.address),
               distance_from_current_location=round(theater.address.distance_from_current_location, 1),
               has_tickets_header=get_formatted_header("Online Tickets?"),
               has_tickets=get_formatted_boolean(theater.has_tickets),
               has_fees_header=get_formatted_header("Fees?"),
               has_fees=get_formatted_boolean(theater.has_fees))


def get_movie_details_cell(movie):
    return """
{title}

{mpaa_rating_header}: {mpaa_rating}
{flixster_rating_header}: {flixster_average_rating}
{rotten_tomatoes_rating_header}: {rotten_tomatoes_rating}

{release_date_header}: {release_date}
{run_time_header}: {run_time}

{actors_header}
{actors}
    """.format(title=get_formatted_movie_title(movie.title),
               release_date_header=get_formatted_header("Release Date"),
               release_date=movie.release_date.strftime("%-m/%-d"),
               mpaa_rating_header=get_formatted_header("MPAA"),
               mpaa_rating=get_formatted_mpaa_rating(movie.mpaa_rating),
               run_time_header=get_formatted_header("Runtime"),
               run_time=movie.run_time,
               actors_header=get_formatted_header("Actors"),
               actors=get_formatted_actors(movie.actors),
               flixster_rating_header=get_formatted_header("Flixster"),
               flixster_average_rating=get_formatted_flixster_rating(movie.flixster_movie_details),
               rotten_tomatoes_rating_header=get_formatted_header("Rotten Tomatoes"),
               rotten_tomatoes_rating=get_formatted_rotten_tomatoes_rating(movie.rotten_tomatoes_movie_details))


def get_formatted_movie_title(title):
    return "\n".join(wrap(get_formatted_header(title), 50))


def get_formatted_header(header):
    return "{bold}{header}{reset}".format(bold=attr("bold"), header=header, reset=attr("reset"))


def get_start_times_row(start_times):
    return [get_formatted_start_times(times) for times in start_times]


def get_formatted_start_times(start_times):
    return "\n".join([start_time.strftime("%-I:%M %p") for start_time in start_times])


def get_formatted_address(address):
    return "\n".join(wrap("{street}, {city}".format(street=address.street, city=address.city), 30))


def get_formatted_actors(actors):
    return "\n".join(wrap(", ".join([actor.name for actor in actors]), 30))


def get_formatted_flixster_rating(flixster_movie_details):
    flixster_rating_percentage = 100 * flixster_movie_details.average_rating / 5
    rating_color = get_movie_rating_percentage_color(flixster_rating_percentage)
    return stylize("{rating} / 5".format(rating=round(flixster_movie_details.average_rating, 1)), fg(rating_color))


def get_formatted_rotten_tomatoes_rating(rotten_tomatoes_movie_details):
    if rotten_tomatoes_movie_details is None:
        return stylize("N/A", fg("red"), attr("bold"))

    rating_color = get_movie_rating_percentage_color(rotten_tomatoes_movie_details.rating)
    return stylize("{rating}".format(rating=rotten_tomatoes_movie_details.rating), fg(rating_color))


def get_formatted_mpaa_rating(rating):
    return stylize(rating, fg(get_mpaa_rating_color(rating)))
