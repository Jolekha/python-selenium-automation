#from time import sleep
#from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then


@given('Open Amazon T&C page')
def open_best_seller_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def store_window(context):
    context.orginal_window = context.driver.current_window_handle


@when('Click on Amazon Privacy Notice link')
def click_link(context):
    context.driver.find_element(By.XPATH,"//a[@href ='https://www.amazon.com/privacy']").click()

@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)

    new_window = context.driver.window_handles[1]
    context.driver.switch_to.window(new_window)

@then('switch back to original')
def switch_to_orginal_window(context):
    context.driver.switch_to.window(context.orginal_window)


@then('Verify Amazon Privacy Notice page is opened')
def verify_the_page(context):
    assert 'https://www.amazon.com/' in context.driver.current_url,f'Url https://www.amazon.com/ not in {context.driver.current_url}'


@then('User can close new window')
def close_window(context):
    context.driver.close()


