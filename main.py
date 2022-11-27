from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


if __name__ == "__main__":
    chrome_driver_path = "C:\Development\chromedriver.exe"
    driver_service = Service(executable_path=chrome_driver_path)
    driver = webdriver.Chrome(service=driver_service)

    url = "http://orteil.dashnet.org/experiments/cookie/"
    driver.get(url)

    # Get cookie to click on
    cookie = driver.find_element(By.ID, value="cookie")

    # Get upgrade item ids
    items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
    item_ids = [item.get_attribute("id") for item in items]

    # Get 5 second timeout and five minute timeout based on current time
    timeout = time.time() + 5
    five_min = time.time() + 60 * 5

    while True:
        cookie.click()

        # Every 5 seconds:
        if time.time() > timeout:
            # Get all upgrade <b> tags
            all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")

            # Convert <b> text into an int
            item_prices = []
            for price in all_prices:
                element_text = price.text
                if element_text != "":
                    cost = int(element_text.split("-")[1].strip().replace(",", ""))
                    item_prices.append(cost)

            # Create dictionary of store items and prices
            cookie_upgrades = {}
            for n in range(len(item_prices)):
                cookie_upgrades[item_prices[n]] = item_ids[n]

            print(cookie_upgrades)

            # Get cookie count
            money_element = driver.find_element(By.ID, value="money").text
            if "," in money_element:
                money_element = money_element.replace(",", "")
            cookie_count = int(money_element)

            # Find upgrades that you can currently afford
            affordable_upgrades = {}
            for cost, id in cookie_upgrades.items():
                if cookie_count > cost:
                    affordable_upgrades[cost] = id

            # Purchase the most expensive affordable upgrade
            try:
                highest_price_affordable_upgrade = max(affordable_upgrades)
                print(highest_price_affordable_upgrade)
            except ValueError:
                pass
            else:
                to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]
                driver.find_element(By.ID, value=to_purchase_id).click()

            # Add another 5 seconds until the next check
            timeout = time.time() + 5

            # After 5 minutes stop the bot and check the cookies per second count.
            if time.time() > five_min:
                cookie_per_s = driver.find_element(By.ID, value="cps").text
                print(cookie_per_s)
                break
