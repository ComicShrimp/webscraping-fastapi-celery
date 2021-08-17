from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class WebBrowser:
    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        self.browser = webdriver.Chrome(
            "/usr/src/app/webdriver/chromedriver", chrome_options=chrome_options
        )

    def get_html_from_url(self, url):
        self.browser.get(url)
        return self.browser.page_source
