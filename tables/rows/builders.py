def build_row(movie_presentations):
    row = [movie_presentations["details"]]
    for theater_id, theater_keys in movie_presentations["theaters"].items():
        for category, start_times in theater_keys["category"].items():
            row.append(", ".join(start_times) + category)

    return row
