from unittest import TestCase

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

