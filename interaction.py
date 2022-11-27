from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

if __name__ == "__main__":
    chrome_driver_path = "C:\Development\chromedriver.exe"
    driver_service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=driver_service)

    url = "https://en.wikipedia.org/wiki/Main_Page"
    driver.get(url)

    article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
    all_portals = driver.find_element(By.LINK_TEXT, value="Roberta Williams")

    search = driver.find_element(By.NAME, value="search")
    search.send_keys("Fart")
    search.send_keys(Keys.ENTER)

