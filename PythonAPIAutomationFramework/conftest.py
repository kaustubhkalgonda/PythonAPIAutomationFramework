import pytest
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import *
from src.utils.utils import Utils
from src.helpers.api_requests_wrapper import *
from src.helpers.common_verifications import *


@pytest.fixture(scope="session")
def create_token():
    response = post_request(url=APIConstants.url_create_token(), auth=None, payload=payload_create_token(),
                            headers=Utils.common_headers_json(), in_json=False)
    return response.json()["token"]


@pytest.fixture(scope="session")
def create_booking():
    response = post_request(url=APIConstants.url_create_booking(), payload=payload_create_booking(),
                            headers=Utils.common_headers_json(), auth=None, in_json=False)
    return response.json()["bookingid"]
