from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def test_mini_project():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(3)
    driver.find_element(By.ID, "btn-make-appointment").click()
    time.sleep(2)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(2)
    driver.find_element(By.ID, "txt-username").send_keys("John Doe")
    driver.find_element(By.ID, "txt-password").send_keys("ThisIsNotAPassword")
    driver.find_element(By.ID, "btn-login").click()
    time.sleep(3)
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
    assert driver.find_element(By.XPATH, "//h2[normalize-space()='Make Appointment']").text == "Make Appointment"
    time.sleep(2)
