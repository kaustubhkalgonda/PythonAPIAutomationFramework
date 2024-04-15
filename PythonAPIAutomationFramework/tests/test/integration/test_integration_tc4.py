# Integration Scenarios
# 4. Create a BOOKING, Delete It

import pytest, allure, time, os
from jsonschema import validate
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import *
from src.utils.utils import Utils
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verifications import *


class TestIntegrationTC4(object):

    @pytest.fixture()
    def create_token(self):
        response = post_request(url=APIConstants.url_create_token(), auth=None, payload=payload_create_token(),
                                headers=Utils.common_headers_json(self), in_json=False)
        return response.json()["token"]

    @pytest.fixture()
    def create_booking(self):
        response = post_request(url=APIConstants.url_create_booking(), payload=payload_create_booking(),
                                headers=Utils.common_headers_json(self=self), auth=None, in_json=False)
        return response.json()["bookingid"]

    @allure.title("Create a BOOKING, Delete It.")
    def test_integration_tc4(self, create_booking, create_token):
        delete_response = delete_request(url=APIConstants.url_update_patch_delete(booking_id=create_booking), auth=None,
                                         headers=Utils.common_headers_patch_put_delete_cookie(token=create_token),
                                         payload={}, in_json=False)
        verify_http_status_code(response_data=delete_response.status_code, expected_data=201)
        assert delete_response.headers["Content-Type"] == "text/plain; charset=utf-8", "Unexpected content-type"
        assert delete_response.text == "Created"