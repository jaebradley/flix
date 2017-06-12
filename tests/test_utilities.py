from unittest import TestCase

from data import PresentationCategory

from tables.utilities import get_category_name, get_mpaa_rating_color, get_movie_rating_percentage_color, \
    get_formatted_boolean, get_category_color


class TestGetCategoryName(TestCase):
    def test_throws_exception_for_unknown_category(self):
        self.assertRaises(ValueError, get_category_name, "jaebaebae")

    def test_returns_for_standard_category(self):
        self.assertEqual("Standard", get_category_name(PresentationCategory.STANDARD))

    def test_returns_3d(self):
        self.assertEqual("3D", get_category_name(PresentationCategory.THREE_D))

    def test_returns_imax(self):
        self.assertEqual("IMAX", get_category_name(PresentationCategory.IMAX))

    def test_returns_4k(self):
        self.assertEqual("4K", get_category_name(PresentationCategory.FOUR_K))

    def test_returns_3d_4k(self):
        self.assertEqual("3D in 4K", get_category_name(PresentationCategory.THREE_D_4K))

    def test_returns_imax_3d(self):
        self.assertEqual("IMAX 3D", get_category_name(PresentationCategory.IMAX_3D))

    def test_imax_3d_4k(self):
        self.assertEqual("IMAX 3D in 4K (aka 'Get over yourself')", get_category_name(PresentationCategory.IMAX_3D_4K))

    def test_imax_3k(self):
        self.assertEqual("IMAX in 4K", get_category_name(PresentationCategory.IMAX_4K))
