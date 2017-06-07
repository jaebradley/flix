def build_row(movie_presentations):
    row = [movie_presentations["details"]]
    for theater_id, theater_keys in movie_presentations["theaters"].items():
        for category, start_times in theater_keys["category"].items():
            row.append(", ".join(start_times) + category)

    return row


def build_theater_metadata_row(theater):
    return """
    Phone Number: {phone_number}\n
    Address: {address}\n
    Distance From Current Location: {distance_from_current_location}\n
    Has Tickets: {has_tickets}\n
    Has Fees: {has_fees}\n
    """
