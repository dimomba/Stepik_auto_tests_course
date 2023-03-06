import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/alert_accept.html")

btn = browser.find_element(By.TAG_NAME, "button")
btn.click()

confirm = browser.switch_to.alert
confirm.accept()

x = browser.find_element(By.ID, "input_value").text
y = calc(x)
ans = browser.find_element(By.ID, "answer")
ans.send_keys(y)

button = browser.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(5)