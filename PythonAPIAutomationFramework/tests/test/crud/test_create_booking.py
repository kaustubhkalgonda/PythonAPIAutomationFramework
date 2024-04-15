import pytest, allure
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_booking
from src.utils.utils import Utils
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verifications import *


class TestCreateBooking(object):
    @allure.title("Verify that status code and booking id is not null.")
    def test_create_booking_positive(self):
        # url, payload, headers
        response = post_request(url=APIConstants.url_create_booking(), payload=payload_create_booking(),
                                headers=Utils.common_headers_json(self=self), auth=None, in_json=False)
        booking_id = response.json()["bookingid"]
        verify_http_status_code(response_data=response.status_code, expected_data=200)
        verify_response_key_not_none(booking_id)

    @allure.title("Verify that status code is 400 when payload is empty.")
    def test_create_booking_empty_payload(self):
        # url, payload, headers
        response = post_request(url=APIConstants.url_create_booking(), payload="",
                                headers=Utils.common_headers_json(self=self), auth=None, in_json=False)
        verify_http_status_code(response_data=response.status_code, expected_data=400)
