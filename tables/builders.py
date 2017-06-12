from textwrap import wrap

from colored import attr, stylize, fg
from terminaltables import SingleTable

from tables.rows.builders import build_rows, build_theater_metadata_row


def build_table(movie_presentations):
    table = SingleTable(get_all_rows(movie_presentations))
    table.inner_row_border = True
    table.justify_columns = get_column_justification(len(movie_presentations.theaters))
    return table.table


def get_all_rows(movie_presentations):
    return [get_headers(movie_presentations.date, movie_presentations.theaters)] + \
           build_rows(movie_presentations.movie_presentations_mapping) + \
           [build_theater_metadata_row(movie_presentations.theaters)]


def get_headers(date, theaters):
    return ["Movies on {date}".format(date=stylize(date.strftime("%-m/%-d"), fg("blue")))] + [get_formatted_theater_header_name(theater.name) for theater in theaters]


def get_formatted_theater_header_name(name):
    return "\n".join(wrap(stylize(name, attr("bold"), attr("underlined")), 30))


def get_column_justification(column_count):
    return {x: "center" for x in range(1, column_count + 1)}
