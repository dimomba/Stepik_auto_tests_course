import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

num1 = int(browser.find_element(By.ID, "num1").text)
num2 = int(browser.find_element(By.ID, "num2").text)
sm = num1 + num2

slct = Select(browser.find_element(By.TAG_NAME, "select"))
slct.select_by_visible_text(str(sm))

submit_btn = browser.find_element(By.TAG_NAME, "button")
submit_btn.click()

time.sleep(10)