import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
menu=driver.find_element_by_id("menu-item-50")
menu.click()
log_mail=driver.find_element_by_id("username")
log_mail.send_keys("1234oleg@mail.ru")
log_password=driver.find_element_by_id("password")
log_password.send_keys("bi-tester-oleg")
time.sleep(3)
login=driver.find_element_by_xpath("//input[@name='login']")
time.sleep(3)
login.click()
time.sleep(3)
lout=driver.find_element_by_link_text("Logout")
lout_text = lout.text
assert "Logout" in lout_text
Text=("ТЕКУЩАЯ СТРАНИЦА:")
url = driver.current_url
print("Элемент LOGOUT обнаружен на странице:", url)
driver.quit()


# #РЕГИСТРАЦИЯ
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
menu=driver.find_element_by_id("menu-item-50")
menu.click()
reg_mail=driver.find_element_by_id("reg_email")
reg_mail.send_keys("1234oleg@mail.ru")
password=driver.find_element_by_id("reg_password")
password.send_keys("bi-tester-oleg")
time.sleep(3)
submit=driver.find_element_by_xpath("//input[@name='register']")
time.sleep(3)
submit.click()
time.sleep(3)
driver.quit()