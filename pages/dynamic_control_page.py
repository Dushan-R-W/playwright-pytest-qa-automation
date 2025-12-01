class DynamicControlPage:
    def __init__ (self, page):
        self.page = page

    def open(self):
        self.page.goto('https://the-internet.herokuapp.com/dynamic_controls')

    def add_checkbox(self):
        self.page.get_by_role("button", name="Add").click()
        
    def remove_checkbox(self):
        self.page.click("button:has-text('Remove')")
        self.page.get_by_text("It's gone!").wait_for(state = "visible")

    def check_box(self):
        self.page.get_by_role("checkbox").check()
    
    def is_checked(self):
        return self.page.get_by_role("checkbox").is_checked()
