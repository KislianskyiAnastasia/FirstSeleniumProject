from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("https://www.w3schools.com/css/css_table.asp")
try:
    # css_in table
    # row
    mexico = driver.find_element(By.CSS_SELECTOR, "#customers tr:nth-child(3)")
    # column
    mexico1 = driver.find_element(By.CSS_SELECTOR, "#customers tr:nth-child(4)>td:nth-child(3)")
    # first row
    item = driver.find_element(By.CSS_SELECTOR, "#customers tr:first-child")
    # last row
    italy = driver.find_element(By.CSS_SELECTOR, "#customers tr:last-child")

finally:
    driver.quit()