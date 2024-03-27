import requests
import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


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
    driver.get("https://www.bet365.com/#/HO/")
    time.sleep(10)


if __name__ == "__main__":
    main()

