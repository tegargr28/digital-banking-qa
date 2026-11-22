from automation.pages.base_page import BasePage


class HomePage(BasePage):
    def load(self, base_url):
        return self.open(base_url)

    def title(self):
        return self.driver.title
