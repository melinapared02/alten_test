from selenium import webdriver


def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.alten.es")
    context.driver.maximize_window()


def after_scenario(context, scenario):
    context.driver.close()
    context.driver.quit()
