from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


driver.implicitly_wait(3)
driver.maximize_window()
driver.get("http://www.kurs-selenium.pl/demo/")
driver.find_element(By.XPATH, "//span[text()='Search by Hotel or City Name']").click()
driver.find_element(By.XPATH, "//div[@id='select2-drop']//input").send_keys("Dubai")
driver.find_element(By.XPATH,"//span[text()='Dubai']").click()
driver.find_element(By.NAME,"checkin").send_keys("05/09/2023")
driver.find_element(By.NAME, "checkout").send_keys("07/09/2023")
driver.find_element(By.ID, "travellersInput").click()
driver.find_element(By.ID,"adultInput").clear()
driver.find_element(By.ID,"adultInput").send_keys("4")
driver.find_element(By.ID,"childInput").clear()
driver.find_element(By.ID,"childInput").send_keys("4")
driver.find_element(By.XPATH,"//button[text()=' Search']").click()
# //h4[contains(@class,'list_title')]//b
hotels = driver.find_elements(By.XPATH,"//h4[contains(@class,'list_title')]//b")
hotel_names = [hotel.get_attribute("textContent") for hotel in hotels]
for name in hotel_names:
    print("Hotel name: " + name)
prices = driver.find_elements(By.XPATH,"//div[contains(@class,'price_tab')]//b")

price_vaiues = [price.get_attribute("textContent") for price in prices]
for price in price_vaiues:
    print("Price is: " + price)

assert hotel_names[0] == "Jumeirah Beach Hotel"
assert hotel_names[1] == "Oasis Beach Tower"
assert hotel_names[2] == "Rose Rayhaan Rotana"
assert hotel_names[3] == "Hyatt Regency Perth"

assert price_vaiues[0] == "$22"
assert price_vaiues[1] == "$50"
assert price_vaiues[2] == "$80"
assert price_vaiues[3] == "$150"

time.sleep(2)
