import pytest, requests, allure


@allure.title("Verify Create Booking")
@allure.description("Verify Create Booking for Restful Booker API.")
@pytest.mark.smoke
def test_create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    url = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=url,headers=headers,json=payload)
    assert response.status_code==200
    response_json = response.json()
    assert response_json["bookingid"] is not None
    assert response_json["booking"]["firstname"]=="Jim"
    assert response_json["booking"]["bookingdates"]["checkin"]=="2018-01-01"


@allure.title("Verify Create Booking with empty payload")
@allure.description("Verify Create Booking for Restful Booker API with empty payload.")
@pytest.mark.smoke
def test_create_booking_empty_payload():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    url = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {}
    response = requests.post(url=url,headers=headers,json=payload)
    assert response.status_code==500