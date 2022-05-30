import booking.constatnts as con
from selenium import webdriver
import os
from booking.booking_filteration import chekcfilteration


class Booking(webdriver.Chrome):
    def __init__(self, path=r"C:/Users/DELL/Desktop/Websraping/chromedriver_win32", teardown=False):
        self.path = path
        os.environ['PATH'] += self.path
        self.teardown = teardown
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(7)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def load(self):
        self.get(con.BASE_URL)

    def choosecurrency(self, currency="Uk"):
        choose = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"]')
        choose.click()
        select = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param="changed_currency=1;selected_currency={currency}" ]')
        select.click()

    def search(self, data):
        searchdata = self.find_element_by_css_selector(
            'input[placeholder="Where are you going?"]'
        )
        searchdata.send_keys(f'{data}')
        adddate = self.find_element_by_css_selector(
            'span[class="sb-date-field__icon sb-date-field__icon-btn bk-svg-wrapper calendar-restructure-sb"]')
        adddate.click()
        seconddate = self.find_element_by_css_selector(
            'td[data-date="2022-05-10"]')
        seconddate.click()
        oneddate = self.find_element_by_css_selector(
            'td[data-date="2022-05-12"]')
        oneddate.click()

    def persons(self):
        person = self.find_element_by_class_name(
            "xp__guests__count")
        person.click()
        minus = self.find_element_by_css_selector(
            'button[aria-label="Decrease number of Adults"]'
        )
        while True:
            minus.click()
            html = self.find_element_by_css_selector(
                'input[data-group-adults-count]'
            )
            value = html.get_attribute('value')
            if int(value) == 1:
                break
        increase = self.find_element_by_css_selector(
            'button[aria-label="Increase number of Adults"]'
        )
        htmlagain = self.find_element_by_css_selector(
            'input[data-group-adults-count]'
        )
        valueagain = htmlagain.get_attribute('max')
        for i in range(int(valueagain)):
            increase.click()
        submit = self.find_element_by_css_selector(
            'button[class="sb-searchbox__button "]'
        )
        submit.click()
        # minus.click()
        # searchclick=self.find_element_by_css_selector('button[data-et-click="      customGoal:cCHObTRVDEZRdPQBcGCfTKYCccaT:1 goal:www_index_search_button_click   "]')
        # searchclick.click()

    def allow(self):
        fetchdata = chekcfilteration(driver=self)
        fetchdata.filterdata(2, 3)
        fetchdata.lowselect(1)
