class CheckBoxPage:
    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto('https://the-internet.herokuapp.com/checkboxes')

    def check(self):
        self.page.get_by_role("checkbox").first.check()

    def uncheck(self):
        self.page.get_by_role("checkbox").nth(1).uncheck()

    def is_checked(self):
        return self.page.get_by_role("checkbox").first.is_checked()
    
    def is_un_checked(self):
        return not self.page.get_by_role("checkbox").nth(1).is_checked()