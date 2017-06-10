import click

from data.services import fetch_parsed_theater_data
from tables.builders import build_table


@click.command()
@click.option("-n", "--name")
def flix(name):
    movie_presentations = fetch_parsed_theater_data(movie_name=name)
    click.echo(build_table(movie_presentations))