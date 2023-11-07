from bs4 import BeautifulSoup as bs4
from selenium import webdriver


class Page:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def get_html(self):
        return self.driver.page_source

    def parse_html(self, html):
        return bs4(html, 'html.parser')

    def prettify(self, soup):
        return soup.prettify()


try:
    chrome = webdriver.Chrome()
    page = Page(chrome)
    page.navigate('https://google.com')
    html = page.get_html()
    soup = page.parse_html(html)
    soup_prettified = page.prettify(soup)
    _as = soup.find_all('a')
    print(_as[0])
except Exception as e:
    print(f'An error occurred: \n {e}')
