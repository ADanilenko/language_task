link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_open_website(browser):
    browser.get(link)
    assert browser.find_elements_by_css_selector("[type='submit'],[class='btn btn-lg btn-primary btn-add-to-basket']"), 'Элемент не найден'














