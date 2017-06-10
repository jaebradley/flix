from textwrap import wrap
from terminaltables import SingleTable
from colored import fg, bg, attr, stylize

from data import PresentationCategory


def build_row(movie_presentations):
    row = [build_movie_metadata_cell(movie_presentations["details"])]
    for theater_id, theater_keys in movie_presentations["theaters"].items():
        if "category" not in theater_keys:
            row.append(stylize("No Times Available", fg("red"), attr("bold")))
        else:
            row.append(build_category_table(theater_keys["category"]))

    return row


def build_theater_metadata_row(theaters):
    return [""] + [build_theater_metadata_cell(theater) for theater in theaters]


def build_theater_metadata_cell(theater):
    return """
{phone_number}
{address}
{distance_from_current_location} mi. away

{has_tickets_header} {has_tickets}
{has_fees_header} {has_fees}
    """.format(phone_number=theater.phone_number,
               address=format_address(theater.address),
               distance_from_current_location=round(theater.address.distance_from_current_location, 1),
               has_tickets_header=format_header("Online Tickets?"),
               has_tickets=format_boolean(theater.has_tickets),
               has_fees_header=format_header("Fees?"),
               has_fees=format_boolean(theater.has_fees))


def build_movie_metadata_cell(movie):
    return """
{title}

{mpaa_rating_header}: {mpaa_rating}
{flixster_rating_header}: {flixster_average_rating}
{rotten_tomatoes_rating_header}: {rotten_tomatoes_rating}

{release_date_header}: {release_date}
{run_time_header}: {run_time}

{actors_header}
{actors}
    """.format(title="\n".join(wrap(format_header(movie.title), 50)),
               release_date_header=format_header("Release Date"),
               release_date=movie.release_date.strftime("%-m/%-d"),
               mpaa_rating_header=format_header("MPAA"),
               mpaa_rating=get_mpaa_rating(movie.mpaa_rating),
               run_time_header=format_header("Runtime"),
               run_time=movie.run_time,
               actors_header=format_header("Actors"),
               actors=format_actors(movie.actors),
               flixster_rating_header=format_header("Flixster"),
               flixster_average_rating=get_flixster_rating(movie.flixster_movie_details),
               rotten_tomatoes_rating_header=format_header("Rotten Tomatoes"),
               rotten_tomatoes_rating=get_rotten_tomatoes_rating(movie.rotten_tomatoes_movie_details))


def format_header(header):
    return "{bold}{header}{reset}".format(bold=attr("bold"), header=header, reset=attr("reset"))


def format_category_start_times(category, start_times):
    return """
{category}
{start_times}
    """.format(category=format_category_name(category), start_times=format_start_times(start_times))


def build_category_table(category_start_times):
    headers = build_category_table_headers(category_start_times.keys())
    rows = build_start_times_row(category_start_times.values())
    table = SingleTable([headers] + [rows])
    table.outer_border = False
    table.inner_heading_row_border = False
    return table.table


def build_category_table_headers(categories):
    return [
        stylize(format_category_name(category), attr("bold"))
        for category in categories
    ]


def build_start_times_row(start_times):
    return [
        format_start_times(times)
        for times in start_times
    ]


def format_start_times(start_times):
    return "\n".join([start_time.strftime("%-I:%M %p") for start_time in start_times])


def get_category_color(category):
    if category == PresentationCategory.STANDARD:
        return "Standard"

    if category == PresentationCategory.THREE_D:
        return "3D"

    if category == PresentationCategory.IMAX:
        return "IMAX"

    if category == PresentationCategory.FOUR_K:
        return "4K"

    if category == PresentationCategory.THREE_D_4K:
        return "3D in 4K"

    if category == PresentationCategory.IMAX_3D:
        return "IMAX 3D"

    if category == PresentationCategory.IMAX_3D_4K:
        return "IMAX 3D in 4K (aka 'Get over yourself')"

    if category == PresentationCategory.IMAX_4K:
        return "IMAX in 4K"

    raise RuntimeError("Unknown category: {category}".format(category=category))


def format_category_name(category):
    if category == PresentationCategory.STANDARD:
        return "Standard"

    if category == PresentationCategory.THREE_D:
        return "3D"

    if category == PresentationCategory.IMAX:
        return "IMAX"

    if category == PresentationCategory.FOUR_K:
        return "4K"

    if category == PresentationCategory.THREE_D_4K:
        return "3D in 4K"

    if category == PresentationCategory.IMAX_3D:
        return "IMAX 3D"

    if category == PresentationCategory.IMAX_3D_4K:
        return "IMAX 3D in 4K (aka 'Get over yourself')"

    if category == PresentationCategory.IMAX_4K:
        return "IMAX in 4K"

    raise RuntimeError("Unknown category: {category}".format(category=category))


def format_address(address):
    return "\n".join(wrap("{street}, {city}".format(street=address.street, city=address.city), 30))


def format_actors(actors):
    return "\n".join(wrap(", ".join([actor.name for actor in actors]), 30))


def get_flixster_rating(flixster_movie_details):
    return stylize("{rating} / 5".format(rating=round(flixster_movie_details.average_rating, 1)),
                   fg(get_movie_rating_percentage_color(100 * flixster_movie_details.average_rating / 5)))


def get_rotten_tomatoes_rating(rotten_tomatoes_movie_details):
    if rotten_tomatoes_movie_details is None:
        return "N/A"

    return stylize("{rating}"
                   .format(rating=rotten_tomatoes_movie_details.rating),
                           fg(get_movie_rating_percentage_color(rotten_tomatoes_movie_details.rating)))


def get_mpaa_rating(rating):
    return stylize(rating, fg(get_mpaa_rating_color(rating)))


def get_mpaa_rating_color(mpaa_rating):
    if mpaa_rating == "G":
        return "green"

    if mpaa_rating == "PG":
        return "blue"

    if mpaa_rating == "PG-13":
        return "yellow"

    if mpaa_rating == "R":
        return "red"

    return "purple"


def get_movie_rating_percentage_color(rating_percentage):
    if rating_percentage < 20:
        return "red"

    if rating_percentage < 40:
        return "yellow"

    if rating_percentage < 60:
        return "magenta"

    if rating_percentage < 80:
        return "blue"

    return "green"


def format_boolean(value):
    return "✔" if value else "✗"

