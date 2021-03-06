from selenium.webdriver.remote.webdriver import WebDriver
from actions.handlers import hello
import re

regex = re.compile('^bleep blop')


def login(browser: WebDriver, username: str, pwd: str) -> WebDriver:
    browser.get('https://mbasic.facebook.com/messages/')
    browser.find_element_by_css_selector('#login_form input[name="email"]').send_keys(username)
    browser.find_element_by_css_selector('#login_form input[name="pass"]').send_keys(pwd)
    browser.find_element_by_css_selector('#login_form input[type="submit"][name="login"]').click()
    return browser


def open_chat(browser: WebDriver, id: str) -> WebDriver:
    browser.get('https://mbasic.facebook.com/messages/read/?tid=cid.' + id)
    return browser


def check_message(browser: WebDriver) -> list:
    ret_m = []
    skip_texts = ['', 'Sent from Mobile', 'Sent from Messenger', 'Sent from Web']
    messages = browser.find_elements_by_css_selector('#messageGroup > div:nth-child(2) span')
    for message in messages:
        text = message.text
        if text in skip_texts:
            continue
        if regex.match(text):
            ret_m = []
        ret_m.append(text)
    return ret_m


def reply_message(browser: WebDriver, m: str) -> WebDriver:
    hello.handle(browser, m)
    return browser


def _send_message(browser: WebDriver, m: str) -> None:
    browser.find_element_by_id('composerInput').send_keys(m)
    browser.find_element_by_css_selector('#composer_form input[type="submit"][name="send"]').click()
