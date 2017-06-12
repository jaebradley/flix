import click

from data.exceptions import InvalidDateException
from data.time import get_date
from data.services import fetch_parsed_theater_data
from tables.builders import build_table

MONTH_CHOICES = [
    "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec",
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"
]

DAY_CHOICES = ["mon", "tue", "wed", "thu", "fri", "sat", "sun",
               "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
               "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]

@click.command()
@click.option("-n", "--name")
@click.option("-t", "--tomorrow", is_flag=True)
@click.option("-m", "--month", type=click.Choice(MONTH_CHOICES))
@click.option("-d", "--day", type=click.Choice(DAY_CHOICES))
@click.option("-l", "--limit", default="2", type=click.Choice(["1", "2", "3", "4", "5"]))
def flix(name, tomorrow, month, day, limit):
    try:
        try:
            date = get_date(use_tomorrow=tomorrow, month=month, day=day)
        except InvalidDateException:
            click.echo("Invalid date inputs")
            return

        movie_presentations = fetch_parsed_theater_data(start_date=date, movie_name=name, limit=limit)

        if len(movie_presentations.movie_presentations_mapping.keys()) > 0:
            click.echo(build_table(movie_presentations))
        else:
            click.echo("No flix found")
    except Exception:
        click.echo("Unable to show any flix")
