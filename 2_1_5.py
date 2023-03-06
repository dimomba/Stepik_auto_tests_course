import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

img_x = browser.find_element(By.ID, "treasure")
x = img_x.get_attribute("valuex")
y = calc(x)

ans = browser.find_element(By.ID, "answer")
ans.send_keys(y)

checkbox = browser.find_element(By.ID, "robotCheckbox")
checkbox.click()

radiobtn = browser.find_element(By.ID, "robotsRule")
radiobtn.click()

submitbtn = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
submitbtn.click()

time.sleep(10)