import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.index_page import IndexPage



@pytest.fixture
def get_chrome_options():
    options = ChromeOptions()
    options.add_argument('chrome')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    driver = webdriver.Chrome(options=get_chrome_options, service=Service(ChromeDriverManager().install()))
    return driver


@pytest.fixture
def setup(get_webdriver):
    url = 'https://www.saucedemo.com/'
    get_webdriver.get(url)
    yield get_webdriver
    get_webdriver.quit()

@pytest.fixture
def index_page(setup):
    yield IndexPage(setup)
