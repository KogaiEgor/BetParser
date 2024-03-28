import requests
import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from match_scraper.matches_scraper import find_esports_soccer_matches


def get_webdriver(port, driver_path):
    chrome_options = Options()
    dr = Service(
        executable_path=driver_path)
    chrome_options.add_experimental_option(
        'debuggerAddress', f'127.0.0.1:{port}')

    driver = webdriver.Chrome(service=dr, options=chrome_options)
    return driver

def get_debug_port(profile_id):
    data = requests.post(
        f'{os.getenv("LOCAL_API")}/start', json={'uuid': profile_id, 'headless': False, 'debug_port': True}
    ).json()
    return data['debug_port']


def main():
    load_dotenv()
    port = get_debug_port(os.getenv('PROFILE_ID'))
    driver = get_webdriver(port, os.getenv('DRIVER_PATH'))
    driver.maximize_window()
    try:
        wait = WebDriverWait(driver, 30)

        driver.get("https://www.bet365.com/#/IP/B151")
        wait.until(
            EC.invisibility_of_element_located((By.XPATH, "//div[contains(@class, 'bl-Preloader_Spinner')]"))
        )
        matches = find_esports_soccer_matches(driver)
        print(matches)
        match = matches[0]
        print("want to click")
        time.sleep(1)

        match.click()
        print("clicked")
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 't')
        time.sleep(4)
        # driver.execute_script("window.open('https://www.bet365.com/#/IP/B1', 'new window')")
        # windows = driver.window_handles
        # print(windows)
        #
        # driver.switch_to.window(windows[1])
        # time.sleep(2)
        # driver.switch_to.window(windows[0])
        # time.sleep(2)
    finally:
        driver.quit()



if __name__ == "__main__":
    main()

