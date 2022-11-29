



# Task-Shop: проверка цены в корзине
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
shop=driver.find_element_by_link_text("Shop")
shop.click()
put_book=driver.find_element_by_xpath("//a[contains(text(),'Add to basket')]")
put_book.click()
time.sleep(3)
item=driver.find_element_by_class_name ("cartcontents")
all_item = item.text
assert "1 " in all_item
time.sleep(3)
price=driver.find_element_by_xpath ("//span[@class='amount']")
all_price = price.text
assert "₹180.00" in all_price
time.sleep(3)
count=driver.find_element_by_class_name('wpmenucart-icon-shopping-cart-0')
count.click()

#LДобавил еще сравнение значений ) что бы цена товара была равна сумме без налога)

price2=driver.find_element_by_xpath("//span[@class='woocommerce-Price-currencySymbol']")
value_price2=price2.text
subtotal=driver.find_element_by_xpath("//span[@class='woocommerce-Price-currencySymbol']")
value_total=subtotal.text
assert value_total == value_price2
print("ЦЕННИК ЧЕСТНЫЙ )))))")


Task-Shop: отображение, скидка товара
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
login.click()
shop=driver.find_element_by_link_text("Shop")
shop.click()
book=driver.find_element_by_xpath("//img[@title='Android Quick Start Guide']")
book.click()
old_price=driver.find_element_by_xpath ("//span[contains(text(),'600')]")
price = old_price.text
assert "600" in price
print("Cтарая цена = 600")
time.sleep(3)
old_price2=driver.find_element_by_xpath ("//span[contains(text(),'450')]")
price2 = old_price2.text
assert "450" in price2
print("Новая цена = 450")
time.sleep(5)
zoom_img= WebDriverWait(driver, 5).until( EC.element_to_be_clickable((By.XPATH, "//img[@title='Android Quick Start Guide']")) )
zoom_img.click()
time.sleep(5)
close= WebDriverWait(driver, 5).until( EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")) )
close.click()
driver.quit()


Task-Shop: сортировка товаров
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
login.click()
shop=driver.find_element_by_link_text("Shop")
shop.click()
selector=driver.find_element_by_css_selector(".orderby")
select = Select(selector)
select.select_by_value("menu_order")
selector.click()
time.sleep(3)
select.select_by_value("price-desc").click
time.sleep(3)
driver.quit()

#Task-Shop: количество товаров в категории
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
log_mail=driver.find_element_by_id("username")
log_mail.send_keys("1234oleg@mail.ru")
log_password=driver.find_element_by_id("password")
log_password.send_keys("bi-tester-oleg")
time.sleep(3)
login=driver.find_element_by_xpath("//input[@name='login']")
login.click()
shop=driver.find_element_by_link_text("Shop")
shop.click()
time.sleep(3)
html=driver.find_element_by_xpath("//a[contains(text(),'HTML')]")
html.click()
time.sleep(5)
items_on_page = driver.find_elements_by_class_name("attachment-shop_catalog.size-shop_catalog.wp-post-image")
time.sleep(5)
if len(items_on_page) == 5:
    print("На странице 3 товара")
else:
    print("Количество товара: " + str(len(items_on_page)))
time.sleep(5)
driver.quit()


TASK-Shop: отображение страницы товара
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
log_mail=driver.find_element_by_id("username")
log_mail.send_keys("1234oleg@mail.ru")
log_password=driver.find_element_by_id("password")
log_password.send_keys("bi-tester-oleg")
time.sleep(3)
login=driver.find_element_by_xpath("//input[@name='login']")
login.click()
shop=driver.find_element_by_link_text("Shop")
shop.click()
book=driver.find_element_by_xpath("//img[@title='Mastering HTML5 Forms']")
book.click()
time.sleep(3)
head=driver.find_element_by_css_selector(".product_title.entry-title")
disc_text = head.text
assert "HTML5 Forms" in disc_text
print("ЗАГОЛОВОК КНИГИ - HTML5 Forms")
driver.quit()




