def build_row(movie_presentations):
    row = [build_movie_metadata_cell(movie_presentations["details"])]
    for theater_id, theater_keys in movie_presentations["theaters"].items():
        for category, start_times in theater_keys["category"].items():
            row.append(", ".join(start_times) + category)

    return row


def build_theater_metadata_row(theaters):
    return [
        build_theater_metadata_cell(theater)
        for theater in theaters
    ]


def build_theater_metadata_cell(theater):
    return """
    Phone Number: {phone_number}\n
    Address: {address}\n
    Distance From Current Location: {distance_from_current_location}\n
    Has Tickets: {has_tickets}\n
    Has Fees: {has_fees}\n
    """.format(phone_number=theater.phone_number,
               address="{street} {city}".format(street=theater.address.street, city=theater.address.city),
               distance_from_current_location=theater.address.distance_from_current_location,
               has_tickets=theater.has_tickets,
               has_fees=theater.has_fees)


def build_movie_metadata_cell(movie):
    return """
    {title}
    Release Date: {release_date}\n
    MPAA: {mpaa_rating}\n
    Runtime: {run_time}\n
    Actors: {actors}\n
    Flixster Avg. Rating: {flixster_average_rating}\n
    Rotten Tomatoes Rating: {rotten_tomatoes_rating}\n
    """.format(title=movie.title,
               release_date=movie.release_date,
               mpaa_rating=movie.mpaa_rating,
               run_time=movie.run_time,
               actors=build_actors(movie.actors),
               flixster_average_rating=movie.flixster_movie_details.average_rating,
               rotten_tomatoes_rating=movie.rotten_tomatoes_movie_details.rating
               )


def build_actors(actors):
    return ", ".join([actor.name for actor in actors])
