import pytest, allure, time, os
from jsonschema import validate
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import *
from src.utils.utils import Utils
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verifications import *


class TestUpdateBooking(object):
    def load_schema(self, file_name):
        with open(file=file_name,mode='r') as file:
            return json.load(file)

    @allure.title("Verify update booking status code")
    def test_update_booking_status_code(self, create_booking, create_token):
        response = put_request(url=APIConstants.url_update_patch_delete(booking_id=create_booking), auth=None,
                               headers=Utils.common_headers_patch_put_delete_cookie(token=create_token),
                               payload=payload_update_booking(), in_json=False)
        verify_http_status_code(response_data=response.status_code, expected_data=200)
        assert response.json()["firstname"]=="Kaustubh"

    @allure.title("Verify response json schema.")
    def test_update_booking_schema(self, create_booking, create_token):
        # url, payload, headers
        response = put_request(url=APIConstants.url_update_patch_delete(booking_id=create_booking), auth=None,
                               headers=Utils.common_headers_patch_put_delete_cookie(token=create_token),
                               payload=payload_update_booking(), in_json=False)
        file_path = os.getcwd() + "/get_booking_schema.json"
        validate(instance=response.json(), schema=self.load_schema(file_path))