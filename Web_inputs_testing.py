from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver=webdriver.Edge()
driver.get("https://practice.expandtesting.com/inputs")
driver.maximize_window()

test_data = [
    {"Number": 90, "Text": "Dhanish", "Password": "Pass@123", "Date": "01-01-2000", "expected": "pass"},
    {"Number": "abc", "Text": "John", "Password": "Pass@123", "Date": "01-01-2000", "expected": "fail"},
    {"Number": 45, "Text": "12345", "Password": "StrongPass@2025", "Date": "13-09-2025", "expected": "fail"},
    {"Number": -10, "Text": "राम", "Password": "Abc!2", "Date": "2025-09-13", "expected": "pass"},
    {"Number": 0, "Text": "This is a sample input", "Password": "password", "Date": "31-02-2025", "expected": "fail"},
    {"Number": 1234567890, "Text": "a", "Password": "Password123", "Date": "13-09-2025", "expected": "pass"}
]
time.sleep(2)
for data in test_data:
    driver.find_element(By.ID,"input-number").clear()
    driver.find_element(By.ID,"input-number").send_keys(data["Number"])
    driver.find_element(By.ID,"input-text").clear()
    driver.find_element(By.ID,"input-text").send_keys(data["Text"])
    driver.find_element(By.ID,"input-password").clear()
    driver.find_element(By.ID,"input-password").send_keys(data["Password"])
    driver.find_element(By.ID,"input-date").clear()
    driver.find_element(By.ID,"input-date").send_keys(data["Date"])

    driver.find_element(By.ID,"btn-display-inputs").click()
    time.sleep(2)


    # print(type(driver.find_element(By.ID, "output-text").text))
    if driver.find_element(By.ID, "output-number").text.strip() == str(data["Number"]).strip():
        print("✅ Test Passed")
    else:
        print("❌ Test Failed")




    

driver.quit()
