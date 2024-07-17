from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import time


driver = webdriver.Chrome()


try:
    driver.get(
        "https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform")
    driver.maximize_window()
    time.sleep(3)
    try:
        driver.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("Susmit Kumar Pandey")

        driver.implicitly_wait(2)
        driver.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("66321019710")

        driver.implicitly_wait(2)
        driver.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("susmitpandey1@gmail.com")

        driver.implicitly_wait(2)
        driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea').send_keys(
            "Sai Apartments,AECS Layout,Bengaluru")

        driver.implicitly_wait(2)
        driver.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("560037")

        driver.implicitly_wait(2)
        driver.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input').send_keys("12-02-2003")

        driver.implicitly_wait(2)
        driver.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys('M')

        driver.implicitly_wait(2)
        code = driver.find_element(By.XPATH, '//*[@id="i30"]/span[1]/b').text
        driver.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(code)

        driver.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()

        time.sleep(2)
        driver.save_screenshot("submission.jpg")

    except NoSuchElementException as e:
        print(e)

except WebDriverException as w:
    print(w)

finally:
    driver.close()
