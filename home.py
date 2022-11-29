import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollTo(0, 600)")
btn_sel=driver.find_element_by_css_selector("a>img[alt='Selenium Ruby']")
btn_sel.click()
btn_sel=driver.find_element_by_css_selector("ul > li.reviews_tab > a")
btn_sel.click()
five_star=driver.find_element_by_css_selector("p > span > a.star-5")
five_star.click()
coment=driver.find_element_by_id('comment')
coment.send_keys("Nice book")
name=driver.find_element_by_id('author')
name.send_keys("Oleg")
mail=driver.find_element_by_id('email')
mail.send_keys("12345@mail.ru")
submit=driver.find_element_by_id('submit')
submit.click()
time.sleep(5)
driver.quit()