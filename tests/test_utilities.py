from unittest import TestCase

from tables.utilities import get_category_name, get_mpaa_rating_color, get_movie_rating_percentage_color, \
    get_formatted_boolean, get_category_color


class TestGetCategoryName(TestCase):
    def test_throws_exception_for_unknown_category(self):
        self.assertRaises(ValueError, get_category_name, "jaebaebae")

