class SecureAreaPage:

    def __init__(self, page):
        self.page = page

    def logout(self):
        self.page.get_by_role("link", name="Logout").click()

    def is_secure_area_visible(self):
        return self.page.get_by_role("heading", name="Secure Area", exact=True).is_visible()
