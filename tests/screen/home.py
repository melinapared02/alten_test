from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.map_element = driver.find_element(By.XPATH, "//div[@id='contacta']")
        self.image = driver.find_element(By.XPATH, "//div[@id='contacta']//img")
        self.data = driver.find_element(
            By.XPATH, "//div[@id='contacta']//div[contains(@class,'marker-detail')]"
        )

    def save_office(self, office):
        self.office_element = self.driver.find_element(
            By.XPATH, f"//div[@id='contacta']//a[@href='#agency-{office}']"
        )

    def save_office_data(self, office):
        self.name_element = self.driver.find_element(
            By.XPATH, f"//div[@id='agency-{office}']//h4"
        )
        self.data_element = self.driver.find_element(
            By.XPATH, f"//div[@id='agency-{office}']//p"
        )
        self.phone_element = self.driver.find_element(
            By.XPATH, f"//div[@id='agency-{office}']/div/span"
        )
