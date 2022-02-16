from pom.base import WebPage
from pom.elements import WebElement, ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        url =  'https://yandex.ru/'
        super().__init__(web_driver, url)  

    # Main search field
    search = WebElement(id='text')

    # Table suggest below the search field
    mini_suggest = WebElement(class_name='mini-suggest__popup-content')

    #Search links for 'tensor.ru' on pages
    links = ManyWebElements(css_selector='#search-result > .serp-item a.link > b')

    # Search button of the main field
    search_run_button = WebElement(xpath='//button[@type="submit"]')

class PagePicture(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://yandex.ru/'
        super().__init__(web_driver, url)  

    # Main search field
    search = WebElement(id='text')
    
    # "Картинки" link with thumbnail
    #picture = WebElement(css_selector='li.services-new__list-item:nth-child(3) > a:nth-child(1) > div:nth-child(2)')
    picture = WebElement(xpath='//li[3]/a/div')
    
    # The first pictures on the top left corner in the "Картинки" page.
    first_category = WebElement(css_selector='div.PopularRequestList-Item:nth-child(1) > a:nth-child(1)')
    
    #Search field subpage
    search_field = WebElement(xpath='/html/body/header/div/div[1]/div[2]/form/div[1]/span/span/input') 
   
    #The first picture on the pictures table
    first_picture = WebElement(xpath='/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]/div/a/img')
   
    
    first_picture_inframe = WebElement(xpath='/html/body/div[13]/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[3]/div/div/img')

    
    button_to_next_picture = WebElement(css_selector='div.CircleButton:nth-child(4)>i')
    
    button_to_previous_picture = WebElement(css_selector='.CircleButton_type_prev > i')