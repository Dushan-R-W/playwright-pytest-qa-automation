from pages.login_page import LoginPage
from pages.secure_area_page import SecureAreaPage


def test_valid_login(page):
    login_page = LoginPage(page)
    secure_area_page = SecureAreaPage(page)

    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert secure_area_page.is_secure_area_visible()

def test_failed_login(page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("testlogin", "SuperSecretPassword!")
    assert login_page.username_error_visible()


def test_login_logout_flow(page):
    login_page = LoginPage(page)
    secure_area_page = SecureAreaPage(page)

    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")

    assert secure_area_page.is_secure_area_visible()

    secure_area_page.logout()
    assert login_page.is_login_page_visible()










