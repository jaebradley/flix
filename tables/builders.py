from textwrap import wrap

from colored import attr, stylize
from terminaltables import SingleTable

from tables.rows.builders import build_rows, build_theater_metadata_row, get_start_times_row
from tables.utilities import get_category_name


def build_table(movie_presentations):
    table = SingleTable(get_all_rows(movie_presentations))
    table.inner_row_border = True
    return table.table


def get_all_rows(movie_presentations):
    return [get_headers(movie_presentations.theaters)] + \
           build_rows(movie_presentations) + \
           [build_theater_metadata_row(movie_presentations.theaters)]


def get_headers(theaters):
    return ["Movies / Theaters"] + [get_formatted_theater_header_name(theater.name) for theater in theaters]


def build_category_table(category_start_times):
    table = SingleTable(get_all_category_table_rows(category_start_times))
    table.outer_border = False
    table.inner_heading_row_border = False
    return table.table


def get_all_category_table_rows(category_start_times):
    return [get_category_table_headers(category_start_times.keys())] + \
           [get_start_times_row(category_start_times.values())]


def get_category_table_headers(categories):
    return [stylize(get_category_name(category), attr("bold")) for category in categories]


def get_formatted_theater_header_name(name):
    return "\n".join(wrap(stylize(name, attr("bold"), attr("underlined")), 30))
