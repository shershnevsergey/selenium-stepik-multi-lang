def test_correct_text_in_add_to_basket_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')

    buy_button_text = browser.find_element_by_css_selector('.btn-add-to-basket').text

    assert buy_button_text == "Añadir al carrito"
