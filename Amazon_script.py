from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# init driver
driver = webdriver.Chrome(executable_path= 'C:\\Users\\17734\\Desktop\\hw\\python-selenium-automation\\chromedriver_win32\\chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/gp/help/customer/display.html')


search = driver.find_element(By.ID, 'helpsearch')
search.send_keys('cancel order', Keys.ENTER)
#actual_result = driver.find_element(By.XPATH, "//div[@class ='help-content']/h1").text
#expected_result = 'Cancel Items or Oders'
#assert expected_result == actual_result, f'Expected{expected_result}, but got {actual_result}'

#driver.quit()
