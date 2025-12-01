from pages.home_page import HomePage

def test_broken_links(page):

    home_page = HomePage(page)
    home_page.open()

    links = page.locator("a").element_handles()
    
    for link in links:
        href = link.get_attribute("href")
        if not href:
            continue
        elif href.startswith("/"):
            full_link = home_page.get_base_url() + href
            response = page.request.get(full_link)
            print(response.status)
            assert response.status < 400 or response.status in [401, 403], f"Broken link: {full_link} ({response.status})"