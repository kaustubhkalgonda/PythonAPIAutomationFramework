import pytest, allure, time
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Utils
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verifications import *


class TestGetBookingIds(object):
    @allure.title("Verify status code is 200")
    def test_get_booking_ids_status_code(self):
        response = get_request(url=APIConstants.url_get_booking_ids(), auth=None)
        verify_http_status_code(response_data=response.status_code, expected_data=200)

    @allure.title("Verify response time is less than 500ms")
    def test_get_booking_ids_response_time(self):
        response = get_request(url=APIConstants.url_get_booking_ids(), auth=None)
        print(response.elapsed.total_seconds())
        assert response.elapsed.total_seconds() < 0.5

    @allure.title("Verify response headers : Content-Type")
    def test_get_booking_ids_response_content_type(self):
        response = get_request(url=APIConstants.url_get_booking_ids(), auth=None)
        assert response.headers["Content-Type"] == "application/json; charset=utf-8", "Unexpected content-type"

    @allure.title("Verify response contains booking ids")
    def test_get_booking_ids_response_contains_bookingid(self):
        response = get_request(url=APIConstants.url_get_booking_ids(), auth=None)
        assert response.json() is not None