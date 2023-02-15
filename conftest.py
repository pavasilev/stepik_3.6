import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru,en,es,fr")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    if user_language == "ru":
        options.add_experimental_option('prefs', {'intl.accept_languages': "ru"})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif user_language == "en":
        options.add_experimental_option('prefs', {'intl.accept_languages': "en"})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif user_language == "es":
        options.add_experimental_option('prefs', {'intl.accept_languages': "es"})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif user_language == "fr":
        options.add_experimental_option('prefs', {'intl.accept_languages': "fr"})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should ru/en/es")
    yield browser
    print("\nquit browser..")
    browser.quit()