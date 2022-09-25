from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time as sl

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service_obj = Service("D:/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR, value="input[type='search']").send_keys('ber')
sl.sleep(4)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
assert count > 0
for result in results:
    button = result.find_element(By.XPATH, './div/button').click()
    
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

# Sum Validation
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum +=int(price.text)

print(sum)

# Check against the promo code we have 
totalAmount = int(driver.find_element(By.CLASS_NAME, 'totAmt').text)
assert sum == totalAmount
print(f"promoCode: {sum} is equal to totalSum: {totalAmount}")

# Discount amount
DiscountAmount = int(driver.find_element(By.CLASS_NAME, 'discountAmt').text)
print(DiscountAmount)
assert DiscountAmount < totalAmount
print("Shetty Coupon works")

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.XPATH, "//button[contains(text(),'Apply')]").click()

wait = WebDriverWait(driver,10)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".promoinfo")))
promoInfo = driver.find_element(By.CLASS_NAME, "promoInfo").text

assert promoInfo == "Code applied ..!"
print("passed")

