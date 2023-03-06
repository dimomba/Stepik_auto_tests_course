import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)

x = browser.find_element(By.ID, "input_value").text
y = calc(x)

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("window.scrollBy(0, 100);")

ans = browser.find_element(By.ID, "answer")
ans.send_keys(y)

checkbox = browser.find_element(By.ID, "robotCheckbox")
checkbox.click()

radiobtn = browser.find_element(By.ID, "robotsRule")
radiobtn.click()

button.click()

time.sleep(5)
