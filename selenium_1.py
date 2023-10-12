from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s = Service(r'C:\Users\sd070\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get('https://ssatem.com/linw/api/searchMain?locale=zh-TW')

server = driver.find_element(By.ID,"serverNameLink")
server.click()
server_selection = input("輸入你想找的服務器")
selection = driver.find_element(By.PARTIAL_LINK_TEXT,server_selection)
selection.click()z

item_name = input("輸入你想要找的物品")
search = driver.find_element(By.ID, "item_name")
search.send_keys(item_name)
time.sleep(0.5)

button = driver.find_element(By.ID,"search_btn")
button.click()
time.sleep(10)

rows = driver.find_elements(By.XPATH,"//*[@id='jsGrid']/div[2]/table/tbody/tr")
for row in rows:
    cells = row.find_elements(By.TAG_NAME,"td")
    server_name = cells[0].text
    item_info = cells[1].text
    quantity = cells[2].text
    price = cells[3].text
    total = cells[4].text

time.sleep(5)
driver.quit()