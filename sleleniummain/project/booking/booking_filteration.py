from selenium.webdriver.remote.webdriver import WebDriver


class chekcfilteration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def filterdata(self, *kwargs):
        maindata = self.driver.find_elements_by_css_selector('div[class=""]')
        for stars in kwargs:
            for i in maindata:
                allstars = i.get_attribute('innerHTML')
                if str(allstars.strip()) == f"{stars} stars":
                    i.click()

    def lowselect(self, values):
        data = self.driver.find_elements_by_css_selector(
            'input[class="f49aa20e67"]')
        for j in data:
            aalvalues = j.get_attribute('value')
            if aalvalues == f'pri={values}':
                j.click()