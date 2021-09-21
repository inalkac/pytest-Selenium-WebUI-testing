"""
    fixtures used in test cases
"""
import pytest
import json
import os
from selenium import webdriver

@pytest.fixture
def browser_config(scope='session'):
    with open("config.json", 'r') as config_file:
        config = json.load(config_file)
    assert config["browser"]  in ["Chrome", "Firefox", "Headless Chrome"]
    return config
    
@pytest.fixture
def browser(browser_config):
    if browser_config["browser"] == "Chrome":
        driver = webdriver.Chrome(executable_path = f"{os.curdir}/webdrivers/chromedriver.exe")
    elif browser_config["browser"] == "Firefox":
        driver = webdriver.Firefox(executable_path = f"{os.curdir}/webdrivers/geckodriver.exe")
    elif browser_config["browser"] == "Headless Chrome":
        opts = webdriver.ChromeOptions()
        opts.add_argument("headless")
        driver = webdriver.Chrome(executable_path = f"{os.curdir}/webdrivers/chromedriver.exe", options = opts)
    else:
        raise Exception(f"browser configuration {browser_config['browser']}, defined in config.json, is not supported")
    driver.maximize_window()
    driver.delete_all_cookies()
    yield driver
    driver.quit()
