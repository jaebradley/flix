
def build_table():
    pass


def build_headers(theaters):
    headers = ["Movies / Theaters"]
    theater_names = [
        theater.name
        for theater in theaters
    ]
    return headers.extend(theater_names)