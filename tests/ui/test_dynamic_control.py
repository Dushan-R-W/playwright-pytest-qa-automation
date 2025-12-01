from pages.dynamic_control_page import DynamicControlPage

def test_check_box(page):
    dynamic_control_page = DynamicControlPage(page)
    dynamic_control_page.open()
    dynamic_control_page.check_box()
    assert dynamic_control_page.is_checked()

def test_remove_input(page):
    dynamic_control_page = DynamicControlPage(page)
    dynamic_control_page.open()
    #dynamic_control_page.add_checkbox()
    dynamic_control_page.remove_checkbox()
    assert page.get_by_text("It's gone!").is_visible()
    