import pytest
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


@pytest.mark.parametrize("username, password, error_method", [
    ("","", "username_error_visible"),
    ("tomsmith","", "password_error_visible"),
    ("","SuperSecretPassword!", "username_error_visible"),
    ("wronguser","wrongpass", "username_error_visible")
])

def test_empty_username_and_password(page, username, password, error_method):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login(username, password)
    assert getattr(login_page, error_method)






