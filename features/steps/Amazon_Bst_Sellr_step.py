from selenium.webdriver.common.by import By
#from selenium import webdriver
from behave import given, when, then
#from time import sleep



@given('Open amazon best seller page')
def open_best_seller_page(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('verify there are 5 links')
def verify_The_Links(context):

     link = len(context.driver.find_elements(By.CSS_SELECTOR,"#zg_tabs div a"))
     assert link == 5, f'Expected 5 links, but got{link}'

