from bs4 import BeautifulSoup as bs4
from selenium import webdriver


class Page:
    def __init__(self, driver):
        self.driver = driver

    def navigate(self, url):
        self.driver.get(url)

    def get_html(self):
        self.html = self.driver.page_source

    def parse_html(self):
        self.soup = bs4(self.html, 'html.parser')

    def prettify(self):
        return self.soup.prettify()


chrome = webdriver.Chrome()

page = Page(chrome)

page.navigate(
    'https://www.reclameaqui.com.br/empresa/reserva/lista-reclamacoes/'
)

page.get_html()

page.parse_html()

soup_prettified = page.prettify()

soup = page.soup

boxes =
