from unittest import TestCase

from mock import patch

from data import Address, Presentation, PresentationCategory, Performance, MovieSchedule, Theater
from data.parsers.theaters import parse_address, parse_presentation, parse_performance, parse_movie_schedules


class TestParseAddress(TestCase):
    def test_returns_address(self):
        street = "street"
        city = "city"
        state = "state"
        zip = "zip"
        longitude = "longitude"
        latitude = "latitude"
        distance_from_current_location = "distance"
        address_details = {
            "street": street,
            "city": city,
            "state": state,
            "zip": zip,
            "longitude": longitude,
            "latitude": latitude,
            "distance": distance_from_current_location
        }
        expected = Address(street=street, city=city, state=state, zip=zip, longitude=longitude, latitude=latitude, distance_from_current_location=distance_from_current_location)
        self.assertEqual(expected, parse_address(address_details))


class TestParsePresentation(TestCase):
    @patch("data.PresentationCategory.identify")
    @patch("data.parsers.theaters.parse_performances")
    def test_returns_presentation(self, mocked_performances_parser, mocked_category_identifier):
        presentation_category = "presentation category"
        parsed_performances = "parsed performances"
        name = "name"
        performances = "performances"
        presentation_details = {
            "name": name,
            "traitGroups": [{
                "performances": performances
            }]
        }
        mocked_performances_parser.return_value = parsed_performances
        mocked_category_identifier.return_value = presentation_category
        expected = Presentation(category=presentation_category, performances=parsed_performances)
        self.assertEqual(expected, parse_presentation(presentation_details))
        mocked_category_identifier.assert_called_once_with(value=name)
        mocked_performances_parser.assert_called_once_with(performances)
