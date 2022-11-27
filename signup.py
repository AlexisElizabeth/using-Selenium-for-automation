from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

if __name__ == "__main__":
    chrome_driver_path = "C:\Development\chromedriver.exe"
    driver_service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=driver_service)

    url = "http://secure-retreat-92358.herokuapp.com/"
    driver.get(url)

    first_name = driver.find_element(By.NAME, value="fName")
    last_name = driver.find_element(By.NAME, value="lName")
    email_address = driver.find_element(By.NAME, value="email")
    sign_up = driver.find_element(By.CSS_SELECTOR, value=".btn")

    first_name.send_keys("Alexis")
    last_name.send_keys("Lastname")
    email_address.send_keys("Alexislastname@gmail.com")
    sign_up.send_keys(Keys.ENTER)
    time.sleep(1000)
