import pytest, os
from dotenv import load_dotenv
@pytest.fixture
def sample_data():
    data = [1,2,3,4,5]
    return data

def test_number1(sample_data):
    load_dotenv()
    print(os.getenv("username"))
    print(os.getenv("password"))
    assert len(sample_data) == 5