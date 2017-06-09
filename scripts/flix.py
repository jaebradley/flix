import click

from tables.builders import build_table
from data.services import fetch_parsed_theater_data


@click.command()
def flix():
    movie_presentations = fetch_parsed_theater_data()
    click.echo(build_table(movie_presentations))