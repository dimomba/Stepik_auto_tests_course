import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'w.txt')           # добавляем к этому пути имя файла
#element.send_keys(file_path)

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")

first_name = browser.find_element(By.NAME, "firstname")
first_name.send_keys("y")

last_name = browser.find_element(By.NAME, "lastname")
last_name.send_keys("y")

email = browser.find_element(By.NAME, "email")
email.send_keys("y")

file_input = browser.find_element(By.CSS_SELECTOR, "[type='file']")
file_input.send_keys(file_path)

button.click()

time.sleep(5)
