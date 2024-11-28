
from selene.support.shared import browser
from selene import be, have


def test_positive(browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene - User-oriented Web UI browser tests in Python'))


def test_negative(browser_open):
    browser.element('[name="q"]').clear().type('log').press_enter()
    browser.element('[id="fbar"]').should(have.text('failed'))


