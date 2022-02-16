from pom.yandex import PagePicture

def test_check_the_aimed_link_is_present(web_browser):
    """ Go to "yandex.ru"
        Link "Картинки" on the pages. """

    page = PagePicture(web_browser)

    presented = page.picture.is_presented()
    assert presented
 
    
def test_has_gone_to_the_right_url(web_browser):
    """ Click on the "Картинки" thumbnail link.
        Check that have switched to the url "https://yandex.ru/images/". """

    page = PagePicture(web_browser)
    page.picture.click()    
    page.switch_to_window(page.window_handles()[1])
    
    current_url = page.get_current_url()[:25]   
    assert current_url == 'https://yandex.ru/images/'


def test_open_the_first_category(web_browser):
    """ Open 1 category, check what opened, 
    in the search for the correct text. """

    page = PagePicture(web_browser)
    page.picture.click()
    page.switch_to_window(page.window_handles()[1])
    name_picture = page.first_category.get_text()
    page.first_category.click()
    text_search_field = page.search_field.get_attribute('value')
    assert name_picture == text_search_field
    

def test_open_the_first_picture(web_browser):
    """Open 1 picture, check what opened. """

    page = PagePicture(web_browser)
    page.picture.click()
    page.switch_to_window(page.window_handles()[1])  
    page.first_category.click()
    
    
    page.first_picture.click()
    assert page.first_picture.is_visible()
    
    
def test_open_the_second_picture(web_browser):
    """ When press the 'forward' button, the picture changes."""

    page = PagePicture(web_browser)
    page.picture.click()
    page.switch_to_window(page.window_handles()[1])  
    page.first_category.click()    
    page.first_picture.click()
    src_first_pic = page.first_picture_inframe.get_attribute('src')
    
    page.button_to_next_picture.move_to_element()    
    page.button_to_next_picture.click()
    
    assert src_first_pic != page.first_picture_inframe.get_attribute('src')
    

    
def test_return_the_first_picture(web_browser):
    """When pressing the 'back' button, the picture changes to the image from step 6.
    Need to check that this is the same image. """

    page = PagePicture(web_browser)
    page.picture.click()
    page.switch_to_window(page.window_handles()[1])  
    page.first_category.click()    
    page.first_picture.click()
    src_first_pic = page.first_picture_inframe.get_attribute('src')
    
    page.button_to_next_picture.move_to_element()   
    page.button_to_next_picture.click()
    
    page.button_to_previous_picture.click()
    
    assert src_first_pic == page.first_picture_inframe.get_attribute('src')