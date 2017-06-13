from unittest import TestCase

from mock import patch

from data import Address, Presentation, Performance, MovieSchedule, Theater
from data.parsers.theaters import parse_address, parse_presentation, parse_performance, parse_movie_schedule, parse_theater


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
    @patch("data.parsers.theaters.parse_performance")
    def test_returns_presentation(self, mocked_performance_parser, mocked_category_identifier):
        presentation_category = "presentation category"
        parsed_performance = "parsed performance"
        name = "name"
        performances = [1, 2]
        presentation_details = {
            "name": name,
            "traitGroups": [{
                "performances": performances
            }]
        }
        mocked_performance_parser.return_value = parsed_performance
        mocked_category_identifier.return_value = presentation_category
        expected = Presentation(category=presentation_category, performances=[parsed_performance, parsed_performance])
        self.assertEqual(expected, parse_presentation(presentation_details))
        mocked_category_identifier.assert_called_once_with(value=name)
        self.assertEqual(2, mocked_performance_parser.call_count)
        mocked_performance_parser.assert_any_call(1)
        mocked_performance_parser.assert_any_call(2)


class TestParsePerformance(TestCase):
    @patch("data.parsers.theaters.parser.parse")
    def test_returns_performance(self, mocked_date_parser):
        iso_date = "isoDate"
        code = "code"
        start_time = "start time"
        performance_details = {
            "isoDate": iso_date,
            "code": code
        }
        mocked_date_parser.return_value = start_time
        expected = Performance(start_time=start_time, code=code)
        self.assertEqual(expected, parse_performance(performance_details))
        mocked_date_parser.assert_called_once_with(iso_date)


class TestParseMovieSchedule(TestCase):
    @patch("data.parsers.theaters.parse_presentation")
    def test_returns_movie_schedule(self, mocked_presentation_parser):
        movie_id = "movie id"
        presentations = [1, 2]
        schedule_detail = {
            "id": movie_id,
            "presentations": presentations
        }
        parsed_presentation = "parsed presentation"
        mocked_presentation_parser.return_value = parsed_presentation
        expected = MovieSchedule(movie_id=movie_id, presentations=[parsed_presentation, parsed_presentation])
        self.assertEqual(expected, parse_movie_schedule(schedule_detail))
        self.assertEqual(2, mocked_presentation_parser.call_count)
        mocked_presentation_parser.assert_any_call(1)
        mocked_presentation_parser.assert_any_call(2)


class TestParseTheater(TestCase):
    @patch("data.parsers.theaters.parse_address")
    @patch("data.parsers.theaters.parse_movie_schedule")
    def test_returns_theater(self, mocked_movie_schedule_parser, mocked_address_parser):
        fid = "fid"
        name = "name"
        has_fees = "has fees"
        has_tickets = "has tickets"
        ticket_source = "ticket source"
        screen_count = "screen count"
        map_uri = "map uri"
        phone_number = "phone number"
        address = "address"
        parsed_address = "parsed address"
        seating = "seating"
        movie_schedules = [1, 2]
        parsed_movie_schedule = "parsed movie schedule"
        theater_details = {
            "id": fid,
            "name": name,
            "hasFees": has_fees,
            "tickets": has_tickets,
            "ticketSource": ticket_source,
            "screens": screen_count,
            "map": map_uri,
            "callablePhone": phone_number,
            "address": address,
            "tags": {
                "seating": seating
            },
            "movies": movie_schedules
        }
        mocked_address_parser.return_value = parsed_address
        mocked_movie_schedule_parser.return_value = parsed_movie_schedule
        expected = Theater(fid=fid, name=name, has_fees=has_fees, has_tickets=has_tickets,
                           screen_count=screen_count, ticket_source=ticket_source, map_uri=map_uri,
                           phone_number=phone_number, address=parsed_address, seating=seating,
                           movie_schedules=[parsed_movie_schedule, parsed_movie_schedule])
        self.assertEqual(expected, parse_theater(theater_details))
