from textwrap import wrap
from terminaltables import SingleTable
from colored import fg, bg, attr, stylize

from tables.rows.builders import build_row, build_theater_metadata_row


def build_table(movie_presentations):
    headers = build_headers(movie_presentations.theaters)
    rows = [
        build_row(movie_presentation)
        for movie_id, movie_presentation in movie_presentations.movie_presentations_mapping.items()
    ]
    theater_metadata_row = build_theater_metadata_row(movie_presentations.theaters)
    all_rows = [headers] + rows + [theater_metadata_row]
    table = SingleTable(all_rows)
    table.inner_row_border = True
    return table.table


def build_headers(theaters):
    headers = ["Movies / Theaters"]
    theater_names = [
        "\n".join(wrap(stylize(theater.name, attr("bold"), attr("underlined")), 30))
        for theater in theaters
    ]
    return headers + theater_names
