from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


if __name__ == "__main__":
    url = "https://www.python.org/"

    chrome_driver_path = "C:\Development\chromedriver.exe"
    driver_service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=driver_service)

    driver.get(url)

    dates = [driver.find_element(By.XPATH,
                                 value=f"//*[@id='content']/div/section/div[3]/div[2]/div/ul/li[{i}]/time").text for i
             in range(1, 6)]
    events = [driver.find_element(By.XPATH,
                                  value=f"//*[@id='content']/div/section/div[3]/div[2]/div/ul/li[{i}]/a").text for i
              in range(1, 6)]

    dictionary = {i: {"time": dates[i], "name": events[i]} for i in range(0, 5)}

    print(dictionary)
