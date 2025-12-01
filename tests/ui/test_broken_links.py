from pages.home_page import HomePage
import requests


def test_broken_urls(page):
    full_links = []
    main_url = "https://the-internet.herokuapp.com"
    page.goto(main_url)
    links = page.locator("a").element_handles()

    for item in links:
        href = item.get_attribute("href")
        if not href:
            continue
        elif href.startswith("/"):
            full_links.append(main_url + href)
    
    for link in full_links:
        response = requests.get(link)
        assert response.status_code < 400 or response.status_code in [200, 401]