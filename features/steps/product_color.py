from selenium.webdriver.common.by import By
#from selenium import webdriver
from behave import given, when, then
#from time import sleep



@given('open amazon product page')
def open_best_seller_page(context):
    context.driver.get('https://www.amazon.com/dp/B081YS2F7N')


@then('user can click select colors')
def very_the_color(context):
    expeted_colors = ['Black', 'Blue', 'Burgundy', 'Caramel', 'Gray', 'Green', 'White']
    color_options = context.driver.find_elements(By.CSS_SELECTOR, "#variation_color_name li" )

    for i in range(len(color_options)):
        color_options[i].click()
        actual_text = context.driver.find_element(By.CSS_SELECTOR, "#variation_color_name span.selection").text
        assert actual_text == expeted_colors[i], f'Error, color is {actual_text}, but expected{expeted_colors[i]}'


