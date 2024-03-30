import pytest, requests, allure


@allure.title("Verify Create Token")
@allure.description("Verify Create Token for Restful Booker API.")
@pytest.mark.smoke
def test_create_token():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/auth"
    url = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=payload)
    response_json = response.json()
    return response_json["token"]


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
    response = requests.post(url=url, headers=headers, json=payload)
    assert response.status_code == 200
    response_json = response.json()
    return response_json["bookingid"]


@allure.title("Verify Update Booking")
@allure.description("Verify Update Booking for Restful Booker API. Take token and booking from previous tests")
@pytest.mark.smoke
def test_update_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(test_create_booking())
    url = base_url + base_path
    headers = {"Content-Type": "application/json",
               "Cookie": test_create_token(),
               "Authorization":"Basic YWRtaW46cGFzc3dvcmQxMjM="}
    payload = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Kitchen"
    }
    response = requests.put(url=url, headers=headers, json=payload)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["firstname"]=="James"
    assert response_json["additionalneeds"] == "Kitchen"