from pages.check_box_page import CheckBoxPage

def test_checkedBoxes(page):
    Check_box_page = CheckBoxPage(page)
    Check_box_page.open()
    Check_box_page.check()
    assert Check_box_page.is_checked()

    Check_box_page.uncheck()
    assert Check_box_page.is_un_checked()
    