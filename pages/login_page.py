class LoginPage:

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto('https://the-internet.herokuapp.com/login')

    def login(self, username, password):
        self.page.get_by_role("textbox", name="Username").fill(username)
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("button", name=" Login").click()
    
    def is_login_page_visible(self):
        return self.page.get_by_role("heading", name="Login Page").is_visible()
    
    def username_error_visible(self):
        return self.page.get_by_text("Your username is invalid! ×").is_visible()
    
    def password_error_visible(self):
        return self.page.get_by_text("Your password is invalid! ×").is_visible()