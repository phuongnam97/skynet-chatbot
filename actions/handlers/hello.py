from actions.facebook import _send_message
from selenium.webdriver.remote.webdriver import WebDriver
import re

regex = re.compile('^hey')


def handle(browser: WebDriver, m: str) -> list:
    if regex.match(m.lower()):
        _send_message(browser, 'bleep blop I\'m a robot')
    return []
