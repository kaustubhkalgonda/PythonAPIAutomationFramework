import pytest, allure
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import *
from src.utils.utils import Utils
from src.helpers.api_requests_wrapper import post_request
from src.helpers.common_verifications import *


class TestCreateToken(object):
    @allure.title("Verify status code is 200")
    def test_create_token_status_code(self):
        response = post_request(url=APIConstants.url_create_token(), auth=None, payload=payload_create_token(),
                                headers=Utils.common_headers_json(self), in_json=False)
        verify_http_status_code(response_data=response.status_code, expected_data=200)

    @allure.title("Verify response headers : Content-Type")
    def test_create_token_response_content_type(self):
        response = post_request(url=APIConstants.url_create_token(), auth=None, payload=payload_create_token(),
                                headers=Utils.common_headers_json(self), in_json=False)
        assert response.headers["Content-Type"] == "application/json; charset=utf-8", "Unexpected content-type"

    @allure.title("Verify response time is less than 500ms")
    def test_create_token_response_time(self):
        response = post_request(url=APIConstants.url_create_token(), auth=None, payload=payload_create_token(),
                                headers=Utils.common_headers_json(self), in_json=False)
        assert response.elapsed.total_seconds() < 0.5

    @allure.title("Verify response token is not null")
    def test_create_token_response_token_value_not_none(self):
        response = post_request(url=APIConstants.url_create_token(), auth=None, payload=payload_create_token(),
                                headers=Utils.common_headers_json(self), in_json=False)
        assert response.json()["token"] is not None, "Token is empty"

