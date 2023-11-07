from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Google:
    def __init__(self, keep_open=True):
        if keep_open:
            options = webdriver.ChromeOptions()
            options.add_experimental_option('detach', True)
            self.driver = webdriver.Chrome(options=options)

        self.url = 'https://google.com'
        self.search_bar_id = 'APjFqb'

    def navigate(self):
        self.driver.get(self.url)

    def search(self, word=''):
        try:
            search_bar = self.driver.find_element(
                by=By.ID, value=self.search_bar_id
            )
            search_bar.clear()  # clear any pre-populated text in the input field
            search_bar.send_keys(word)   # input text
            search_bar.send_keys(Keys.RETURN)   # press enter
        except Exception as e:
            print(f'An error occurred while searching: \n {str(e)}')


g = Google()
g.navigate()
g.search('Web Scraping with Selenium')
