class HomePage:

    def __init__ (self, page):
        self.page = page

    def open(self):
        self.page.goto('https://the-internet.herokuapp.com')

    def get_base_url(self):
        return "https://the-internet.herokuapp.com"

