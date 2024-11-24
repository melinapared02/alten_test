import time

from behave import given, then, when
from selenium.webdriver.common.action_chains import ActionChains

from tests.screen.home import HomePage


@given("I am on the home page")
def go_to_home_page(context):
    context.home_page = HomePage(context.driver)


@when("I go to the map section")
def go_to_map_section(context):
    actions = ActionChains(context.driver)
    actions.scroll_to_element(context.home_page.map_element).scroll_by_amount(
        0, 200
    ).perform()
    time.sleep(0.2)


@then("I verify that the map is visible")
def verify_map_is_visible(context):
    assert context.home_page.image.is_displayed(), "the map is not visible"


@then("I verify that the office data is visible")
def verify_office_data_is_visible(context):
    assert context.home_page.data.is_displayed(), "the office data is not visible"


@when("select the office {office}")
def select_office(context, office):
    context.home_page.save_office(office)
    context.home_page.office_element.click()


@then("I verify that the data of the office {office} are {name}, {data} and {phone}")
def verify_office_data_is_correct(context, office, name, data, phone):
    context.home_page.save_office_data(office)

    assert (
        context.home_page.name_element.text == name
    ), f"the name of the office must be '{name}', but it is '{context.home_page.name_element.text}'"
    assert (
        context.home_page.data_element.text.replace("\n", " ") == data
    ), f"the data of the office must be '{data}', but it is '{context.home_page.data_element.text.replace('\n', ' ')}'"
    assert (
        context.home_page.phone_element.text == phone
    ), f"the phone of the office must be '{phone}', but it is '{context.home_page.phone_element.text}'"
