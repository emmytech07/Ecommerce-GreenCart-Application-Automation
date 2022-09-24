from lib2to3.pgen2 import driver
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service("D:/chromedriver/chromedriver")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
