import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
btn = browser.find_element(By.TAG_NAME, "button")
btn.click()

#browser.switch_to.window(browser.window_handles[1])

x = browser.find_element(By.ID, "input_value").text
y = calc(x)
ans = browser.find_element(By.ID, "answer")
ans.send_keys(y)

button = browser.find_element(By.ID, "solve")
button.click()

time.sleep(5)
