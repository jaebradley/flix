from textwrap import wrap

from colored import attr, stylize
from terminaltables import SingleTable

from tables.rows.builders import build_row, build_theater_metadata_row, get_start_times_row
from tables.utilities import get_category_name


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


def build_category_table(category_start_times):
    headers = get_category_table_headers(category_start_times.keys())
    rows = get_start_times_row(category_start_times.values())
    table = SingleTable([headers] + [rows])
    table.outer_border = False
    table.inner_heading_row_border = False
    return table.table


def get_category_table_headers(categories):
    return [
        stylize(get_category_name(category), attr("bold"))
        for category in categories
    ]
