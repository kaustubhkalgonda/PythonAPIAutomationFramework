from faker import Faker

fake = Faker()


def payload_create_booking():
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
    return payload

def payload_update_booking():
    payload = {
        "firstname": "Kaustubh",
        "lastname": "Kalgonda",
        "totalprice": 555,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2023-01-08"
        },
        "additionalneeds": "Kitchen"
    }
    return payload

def payload_create_booking_dynamic_data():
    payload = {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(100, 1000),
        "depositpaid": fake.boolean(),
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": fake.random_elements(elements=("Breakfast", "Parking", "Kitchen"))
    }
    return payload


def payload_create_token():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload
