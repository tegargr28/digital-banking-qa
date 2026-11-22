
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver():
    options = Options()

    options.add_argument("--start-maximized")

    # Keep Chrome open after the Selenium session ends
    options.add_experimental_option("detach", True)

    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    if os.path.exists(chrome_path):
        options.binary_location = chrome_path

    driver = webdriver.Chrome(options=options)

    return driver
