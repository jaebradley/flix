def build_row(movie_presentations):
    row = [build_movie_metadata_cell(movie_presentations["details"])]
    for theater_id, theater_keys in movie_presentations["theaters"].items():
        if "category" not in theater_keys:
            row.append("N/A")
        else:
            for category, start_times in theater_keys["category"].items():
                formatted_start_times = [start_time.strftime("%-I:%M %p") for start_time in start_times]
                row.append(", ".join(formatted_start_times))

    return row


def build_theater_metadata_row(theaters):
    row = [""]

    for theater in theaters:
        row.append(build_theater_metadata_cell(theater))

    return row


def build_theater_metadata_cell(theater):
    return """
    Phone Number: {phone_number}
    Address: {address}
    Distance From Current Location: {distance_from_current_location}
    Has Tickets: {has_tickets}
    Has Fees: {has_fees}
    """.format(phone_number=theater.phone_number,
               address="{street}, {city}".format(street=theater.address.street, city=theater.address.city),
               distance_from_current_location=round(theater.address.distance_from_current_location, 2),
               has_tickets=theater.has_tickets,
               has_fees=theater.has_fees)


def build_movie_metadata_cell(movie):
    rotten_tomatoes_rating = "N/A" if movie.rotten_tomatoes_movie_details is None else movie.rotten_tomatoes_movie_details.rating


    return """
    {title}
    Release Date: {release_date}
    MPAA: {mpaa_rating}
    Runtime: {run_time}
    Flixster Avg. Rating: {flixster_average_rating}
    Rotten Tomatoes Rating: {rotten_tomatoes_rating}
    """.format(title=movie.title,
               release_date=movie.release_date,
               mpaa_rating=movie.mpaa_rating,
               run_time=movie.run_time,
               actors=build_actors(movie.actors),
               flixster_average_rating=movie.flixster_movie_details.average_rating,
               rotten_tomatoes_rating=rotten_tomatoes_rating)


def build_actors(actors):
    return ", ".join([actor.name for actor in actors])
