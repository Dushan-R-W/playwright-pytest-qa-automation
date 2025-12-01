from pages.api_page import APIpage
import time
import pytest
import requests

@pytest.fixture
def api_page():
    return APIpage("https://the-internet.herokuapp.com")

def test_login_success(api_page):
    response = api_page.request_get("/login")
    assert response.status_code == 200

def test_non_existent_page(api_page):
    #url = "https://the-internet.herokuapp.com/non-existent-page"
    payload = {"username": "wronguser", "password": "wrongpass"}
    #response = requests.post(url, data=payload)
    response = api_page.request_post("/non-existent-page", payload)
    assert response.status_code == 404

def test_redirect(api_page):
    response = api_page.request_get_no_redirect("/secure")
    assert response.status_code in [301, 302]
    assert "/login" in response.headers.get('Location', "")

def test_header_exists(api_page):
    response = api_page.request_get("/login")
    assert "Content-Type" in response.headers, "No headder"

def test_login_page_response_time(api_page):

    start_time = time.time()
    response = api_page.request_get("/login")
    end_time = time.time()

    elapsed_time = end_time - start_time
    assert response.status_code == 200
    assert elapsed_time < 1, f"Page took too long: {elapsed_time}"

