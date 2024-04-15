
def verify_http_status_code(response_data, expected_data):
    assert int(response_data) == expected_data, "Expected Status Code is " + str(expected_data)

def verify_json_key_for_not_null(key):
    assert key != 0, "Key is non empty "+key
    assert key>0, "Key is greater than Zero"

def verify_response_key_not_none(key):
    assert key is not None