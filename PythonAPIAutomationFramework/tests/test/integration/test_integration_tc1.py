# Integration Scenarios

# 1. Verify that Create Booking -> Patch Request - Verify that firstName is updated.

import pytest, allure, time, os
from jsonschema import validate
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import *
from src.utils.utils import Utils
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verifications import *
class TestIntegrationTC1(object):
    @pytest.fixture()
    def create_token(self):
        response = post_request(url=APIConstants.url_create_token(), auth=None, payload=payload_create_token(),
                                headers=Utils.common_headers_json(), in_json=False)
        return response.json()["token"]

    @pytest.fixture()
    def create_booking(self):
        response = post_request(url=APIConstants.url_create_booking(), payload=payload_create_booking(),
                                headers=Utils.common_headers_json(), auth=None, in_json=False)
        return response.json()["bookingid"]

    @allure.title("Verify that Create Booking -> Patch Request - Verify that firstName is updated.")
    def test_integration_tc1(self, create_booking, create_token):
        response = patch_request(url=APIConstants.url_update_patch_delete(booking_id=create_booking), auth=None,
                               headers=Utils.common_headers_patch_put_delete_cookie(token=create_token),
                               payload=payload_partial_update_booking(), in_json=False)
        verify_http_status_code(response_data=response.status_code, expected_data=200)
        assert response.headers["Content-Type"] == "application/json; charset=utf-8", "Unexpected content-type"
        assert response.json()["firstname"] == "Kaustubh"
        assert response.json()["lastname"] == "Kalgonda"
