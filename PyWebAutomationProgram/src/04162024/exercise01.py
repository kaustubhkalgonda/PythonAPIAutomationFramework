from selenium import webdriver

def test_open_google():
    driver = webdriver.Chrome()
    driver.get("http://www.google.com")
    print(driver.title)
    assert driver.title=="Google"