
#Open browser
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.get("https://telranedu.web.app/login")
    # driver.get("https://icarro-v1.netlify.app/search?page=0&size=10")
    #by TAG_NAME

    div = driver.find_elements(By.TAG_NAME, "div")
    print(len(div))
    div2 = driver.find_element(By.CSS_SELECTOR, "div")
    #div3 = driver.find_element(By.XPATH, "div")

    h1 = driver.find_element(By.TAG_NAME, "h1")
    h1_2 = driver.find_element(By.CSS_SELECTOR, "h1")

    input = driver.find_element(By.TAG_NAME, "input")
    input1 = driver.find_element(By.TAG_NAME, "input")

    a_list = driver.find_elements(By.TAG_NAME, "a")
    a_list_1 = driver.find_element(By.CSS_SELECTOR, "a")
    print(len(a_list))

    #by class
    container = driver.find_element(By.CLASS_NAME, "container")
    container_1 = driver.find_elements(By.CSS_SELECTOR, ".container")
    nav_bar = driver.find_elements(By.CLASS_NAME, "active")
    nav_bar_1 = driver.find_elements(By.CSS_SELECTOR, "active")
    print(len(nav_bar))
    print(len(nav_bar_1))

    login_1 = driver.find_element(By.CLASS_NAME, "login_login__3EHKB")
    login_1_1 = driver.find_elements(By.CSS_SELECTOR, ".login_login__3EHKB")

    #by id
    root = driver.find_element(By.ID, "root")
    root_1 = driver.find_element(By.CSS_SELECTOR, "#root")
    root_2 = driver.find_elements(By.ID, "root")
    print(len(root_2))

    # by attribute
    name = driver.find_element(By.CSS_SELECTOR,'input[name="email"]')
    email =driver.find_element(By.CSS_SELECTOR,'input[name=\"email\"]')

#     subtitle = driver.find_element(By.CSS_SELECTOR,'[class*="Type your data and hit Yalla!"]')
#     start_sub = driver.find_element(By.CSS_SELECTOR,)
finally:
    driver.quit()
