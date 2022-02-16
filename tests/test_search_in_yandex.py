from pom.yandex import MainPage
import time

def test_check_search_field(web_browser):
    """ Go to "yandex.ru".
        Check the presence of a search field. """

    page = MainPage(web_browser)

    presented = page.search.is_presented()
    assert presented
  
    
def test_that_appeared_the_table_with_suggest(web_browser):
    """ Type in search "Тензор".
        Check that a table with hints (suggest) has appeared. """

    page = MainPage(web_browser)
    page.search = 'Тензор'
    time.sleep(1)
    
    visible = page.mini_suggest.is_visible()
    assert visible   
   
    
def test_first_five_page_have_link(web_browser):
    """ When press Enter, a table of search results appears.
        The first 5 results have a link to "tensor.ru". """

    page = MainPage(web_browser)
    page.search = 'Тензор'
    page.search_run_button.click()
     
    links = page.links.get_text()
    items = [element for element in links[:5]]
    count = 0
    for i in items:
        if i == 'tensor.ru':
            count += 1
    if count != 5:
        raise Exception(f'Not all pages have aimed link, outcome-the {count} pages have a "tensor.ru" link.')