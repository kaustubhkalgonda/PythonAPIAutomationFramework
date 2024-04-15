# Integration Scenarios
# 3. Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.

import pytest, allure, time, os, random
from jsonschema import validate
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import *
from src.utils.utils import Utils
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verifications import *


class TestIntegrationTC3(object):

    def load_schema(self, file_name):
        with open(file=file_name,mode='r') as file:
            return json.load(file)
    @pytest.fixture()
    def create_token(self):
        response = post_request(url=APIConstants.url_create_token(), auth=None, payload=payload_create_token(),
                                headers=Utils.common_headers_json(self), in_json=False)
        return response.json()["token"]

    @pytest.fixture()
    def get_booking_id(self):
        response = get_request(url=APIConstants.url_get_booking_ids(), auth=None)
        return response.json()[random.randint(1, 100)]["bookingid"]

    @allure.title("Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.")
    def test_integration_tc3(self, get_booking_id, create_token):
        # url, payload, headers
        response = put_request(url=APIConstants.url_update_patch_delete(booking_id=get_booking_id), auth=None,
                               headers=Utils.common_headers_patch_put_delete_cookie(token=create_token),
                               payload=payload_update_booking(), in_json=False)
        verify_http_status_code(response_data=response.status_code, expected_data=200)
        get_response = get_request(url=APIConstants.url_get_booking(get_booking_id), auth=None)
        verify_http_status_code(response_data=get_response.status_code, expected_data=200)
        file_path = os.getcwd() + "/get_booking_schema.json"
        validate(instance=get_response.json(), schema=self.load_schema(file_path))
        assert response.json()["firstname"] == "Kaustubh"
