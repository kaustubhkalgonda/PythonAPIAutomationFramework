# Integration Scenarios
# 5. Invalid Creation - enter a wrong payload or Wrong JSON.
import pytest, allure, time, os
from jsonschema import validate
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import *
from src.utils.utils import Utils
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verifications import *


class TestIntegrationTC5(object):

    @allure.title("Invalid Creation - enter a wrong payload or Wrong JSON.")
    def test_integration_tc5(self):
        response = post_request(url=APIConstants.url_create_booking(), payload=invalid_payload_create_booking(),
                                headers=Utils.common_headers_json(self=self), auth=None, in_json=False)
        verify_http_status_code(response_data=response.status_code, expected_data=500)
        assert response.text == "Internal Server Error"