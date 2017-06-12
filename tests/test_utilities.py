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


class TestGetMovieRatingPercentageColor(TestCase):
    def test_throws_exception_for_unexpected_rating(self):
        self.assertRaises(ValueError, get_movie_rating_percentage_color, "jaebaebae")

    def test_returns_color_for_rating_percentage_less_than_20(self):
        self.assertEqual("red", get_movie_rating_percentage_color(10))

    def test_returns_color_for_rating_percentage_less_than_40(self):
        self.assertEqual("yellow", get_movie_rating_percentage_color(30))

    def test_returns_color_for_rating_percentage_less_than_60(self):
        self.assertEqual("magenta", get_movie_rating_percentage_color(50))

    def test_returns_color_for_rating_percentage_less_than_80(self):
        self.assertEqual("blue", get_movie_rating_percentage_color(70))

    def test_returns_color_for_rating_percentage_less_than_or_equal_to_100(self):
        self.assertEqual("green", get_movie_rating_percentage_color(100))


class TestGetFormattedBoolean(TestCase):
    def test_true_returns_checkmark(self):
        self.assertEqual("✔", get_formatted_boolean(True))

    def test_false_returns_x(self):
        self.assertEqual("✗", get_formatted_boolean(False))


class TestGetCategoryColor(TestCase):
    def test_throws_exception_for_unknown_category(self):
        self.assertRaises(ValueError, get_category_color, "jaebaebae")

    def test_standard(self):
        self.assertEqual("blue", get_category_color(PresentationCategory.STANDARD))

    def test_three_d(self):
        self.assertEqual("green", get_category_color(PresentationCategory.THREE_D))

    def test_imax(self):
        self.assertEqual("red", get_category_color(PresentationCategory.IMAX))

    def test_four_k(self):
        self.assertEqual("yellow", get_category_color(PresentationCategory.FOUR_K))

    def test_three_d_four_k(self):
        self.assertEqual("purple", get_category_color(PresentationCategory.THREE_D_4K))

    def test_imax_3d(self):
        self.assertEqual("cyan", get_category_color(PresentationCategory.IMAX_3D))

    def test_imax_3d_4k(self):
        self.assertEqual("orange", get_category_color(PresentationCategory.IMAX_3D_4K))

    def test_imax_4k(self):
        self.assertEqual("magenta", get_category_color(PresentationCategory.IMAX_4K))
