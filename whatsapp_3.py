from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import sys
import schedule


def send_periodic_msg():

    targetesh = '"Private"'
    msg_contentesh = 'Sample Message'
    x_argesh = '//span[contains(@title,' + targetesh + ')]'
    private = wait.until(EC.presence_of_element_located((By.XPATH,x_argesh)))
    private.click()

    sample_message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
    sample_message.send_keys(msg_contentesh)

    sample_send = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
    sample_send.click()
    print('Message sent')




def send_msg():

    target = '"QPL auction 2020"'

    msg_content = "Stadium: MA Chidambaram Stadium.If already taken,then Arun Jaitley Stadium."

    x_arg = '//span[contains(@title,' + target + ')]'

    group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    group_title.click()

    message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
    message.send_keys(msg_content)

    send = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
    send.click()

    driver.close()

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 100)

schedule.every().saturday.at('09:00').do(send_msg)
schedule.every(1).minutes.do(send_periodic_msg)

while 1:
     schedule.run_pending()
     time.sleep(1)

