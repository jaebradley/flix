from textwrap import wrap

from colored import fg, attr, stylize

from tables.utilities import get_mpaa_rating_color, get_movie_rating_percentage_color, get_formatted_boolean, \
    get_category_name, get_category_color


def build_rows(movie_presentations_mapping):
    return [build_row(movie_presentations) for movie_presentations in movie_presentations_mapping.values()]


def build_row(movie_presentations):
    row = [get_movie_details_cell(movie_presentations["details"])]
    for theater_id, theater_keys in movie_presentations["theaters"].items():
        if "category" not in theater_keys:
            row.append(stylize("No Times Available", fg("red"), attr("bold")))
        else:
            row.append(build_categories_start_times(theater_keys["category"]))

    return row


def build_theater_metadata_row(theaters):
    return [""] + [get_theater_details_cell(theater) for theater in theaters]


def build_categories_start_times(categories):
    return "\n".join([
        build_category_start_times(category, start_times)
        for category, start_times in categories.items()
    ])


def build_category_start_times(category, start_times):
    return """
{category}
{start_times}
    """.format(category=get_formatted_category(category),
               start_times=get_formatted_start_times(start_times))


def get_theater_details_cell(theater):
    return """
{phone_number}
{street}
{city}
{distance_from_current_location} mi. away
    """.format(phone_number=get_formatted_header(theater.phone_number),
               street=get_formatted_street(theater.address.street),
               city=get_formatted_city(theater.address.city),
               distance_from_current_location=round(theater.address.distance_from_current_location, 1),
               has_tickets_header=get_formatted_header("Online Tickets?"),
               has_tickets=get_formatted_boolean(theater.has_tickets))


def get_movie_details_cell(movie):
    return """
{title}

{mpaa_rating_header}: {mpaa_rating}
{flixster_rating_header}: {flixster_average_rating}
{rotten_tomatoes_rating_header}: {rotten_tomatoes_rating}

{release_date_header}: {release_date}
{run_time_header}: {run_time}
    """.format(title=get_formatted_movie_title(movie.title),
               release_date_header=get_formatted_header("Release Date"),
               release_date=movie.release_date if movie.release_date is None else movie.release_date.strftime("%-m/%-d"),
               mpaa_rating_header=get_formatted_header("MPAA"),
               mpaa_rating=get_formatted_mpaa_rating(movie.mpaa_rating),
               run_time_header=get_formatted_header("Runtime"),
               run_time=movie.run_time,
               flixster_rating_header=get_formatted_header("Flixster"),
               flixster_average_rating=get_formatted_flixster_rating(movie.flixster_movie_details),
               rotten_tomatoes_rating_header=get_formatted_header("Rotten Tomatoes"),
               rotten_tomatoes_rating=get_formatted_rotten_tomatoes_rating(movie.rotten_tomatoes_movie_details))


def get_formatted_movie_title(title):
    return "\n".join([get_formatted_header(part) for part in wrap(title, 30)])


def get_formatted_header(header):
    return "{bold}{header}{reset}".format(bold=attr("bold"), header=header, reset=attr("reset"))


def get_start_times_row(start_times):
    return [get_formatted_start_times(times) for times in start_times]


def get_formatted_start_times(start_times):
    return "\n".join([start_time.strftime("%-I:%M %p") for start_time in start_times])


def get_formatted_street(street):
    return "\n".join(wrap(get_formatted_header("{street}".format(street=street)), 30))


def get_formatted_city(city):
    return "\n".join(wrap(get_formatted_header("{city}".format(city=city)), 30))


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


def get_formatted_category(category):
    return stylize(get_formatted_header(get_category_name(category)), fg(get_category_color(category)))
