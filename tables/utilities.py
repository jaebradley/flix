from data import PresentationCategory


def get_category_name(category):
    if category == PresentationCategory.STANDARD:
        return "Standard"

    if category == PresentationCategory.THREE_D:
        return "3D"

    if category == PresentationCategory.IMAX:
        return "IMAX"

    if category == PresentationCategory.FOUR_K:
        return "4K"

    if category == PresentationCategory.THREE_D_4K:
        return "3D in 4K"

    if category == PresentationCategory.IMAX_3D:
        return "IMAX 3D"

    if category == PresentationCategory.IMAX_3D_4K:
        return "IMAX 3D in 4K (aka 'Get over yourself')"

    if category == PresentationCategory.IMAX_4K:
        return "IMAX in 4K"

    raise ValueError("Unknown category: {category}".format(category=category))


def get_mpaa_rating_color(mpaa_rating):
    if mpaa_rating == "G":
        return "green"

    if mpaa_rating == "PG":
        return "blue"

    if mpaa_rating == "PG-13":
        return "yellow"

    if mpaa_rating == "R":
        return "red"

    return "plum_4"


def get_movie_rating_percentage_color(rating_percentage):
    if rating_percentage < 20:
        return "red"

    if rating_percentage < 40:
        return "yellow"

    if rating_percentage < 60:
        return "magenta"

    if rating_percentage < 80:
        return "blue"

    if rating_percentage <= 100:
        return "green"

    raise ValueError("Unexpected rating percentage: {rating_percentage}".format(rating_percentage=rating_percentage))


def get_formatted_boolean(value):
    return "✔" if value else "✗"


def get_category_color(category):
    if category == PresentationCategory.STANDARD:
        return "blue"

    if category == PresentationCategory.THREE_D:
        return "green"

    if category == PresentationCategory.IMAX:
        return "red"

    if category == PresentationCategory.FOUR_K:
        return "yellow"

    if category == PresentationCategory.THREE_D_4K:
        return "plum_4"

    if category == PresentationCategory.IMAX_3D:
        return "cyan"

    if category == PresentationCategory.IMAX_3D_4K:
        return "orange"

    if category == PresentationCategory.IMAX_4K:
        return "magenta"

    raise ValueError("Unknown category: {category}".format(category=category))
