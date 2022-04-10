from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chromedriver = "/Users/yongjer/Downloads/chromedriver"

option = webdriver.ChromeOptions()

option.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'

s = Service(chromedriver)

driver = webdriver.Chrome(service=s, options=option)

driver.get("https://cu.nsysu.edu.tw/mooc/login.php")

id = driver.find_element(By.ID,"s_username")

id.send_keys("YourId")

passward = driver.find_element(By.NAME,"password")

passward.send_keys("YourPassword")

send = driver.find_element(By.ID,"btnSignIn")

send.click()


