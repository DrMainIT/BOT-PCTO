from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException

browser = webdriver.Chrome('/Users/francesco/Downloads/chromedriver_mac_arm64/chromedriver')
browser.get('https://www.educazionedigitale.it/goccedisostenibilita/moduli-formativi/')

browser.maximize_window()
#reject cookie
browser.find_element(By.XPATH,'/html/body/div[3]/div/div/div/div[2]/button[3]').click()

#form 
browser.find_element(By.XPATH,'/html/body/div[5]/header/div/div[2]/div[1]/div[4]/ul/li[5]/a').click()
sleep(0.3)
browser.find_element(By.ID,'user').send_keys('stu-9148302-04')
sleep(0.1)
browser.find_element(By.ID,'pass').click()
sleep(0.1)
browser.find_element(By.ID,'pass').send_keys('i2h0z5')


sleep(0.1)
browser.find_element(By.NAME,'invia').submit()
sleep(0.3)
try:
    browser.find_element(By.XPATH,'/html/body/div[2]/div/div[1]/div/div[2]/div/div/form/input[2]').click()
    sleep(0.3)
    browser.find_element(By.NAME,'invia').submit()
except:
    pass



'''

for x in range(1,11):
    sleep(0.3)
    browser.find_element(By.XPATH,f'/html/body/div[5]/main/div[2]/div[2]/section[1]/div[2]/div/div/div/table/tbody/tr[{x}]/td[2]/div[2]/a').click()
    for i in range(2,5):
        sleep(0.3)
        for j in range(1,4):
            sleep(0.3)
            p = browser.find_element(By.XPATH,f'/html/body/div[5]/main/div[2]/div/div/div/form/div[{i}]/p[{j}]/input')
            val = p.get_attribute('value')
            if val == '1':
                sleep(0.5)
                browser.execute_script("arguments[0].click();",p)
    sleep(4)
    
    try:
        alert = browser.switch_to.alert

         # print hello if alert is present
        print("hello")

        # close the alert box
        alert.accept()
        sleep(1)
    except NoAlertPresentException:
    # print nothing if no alert is present
        pass
    browser.find_element(By.XPATH,f'/html/body/div[5]/main/div[2]/div/div/div/p/input').click()


'''




    




for x in range(1,11):
    sleep(0.3)
    browser.find_element(By.XPATH,f'/html/body/div[5]/main/div[2]/div[2]/section[2]/div[2]/div/div/div/table/tbody/tr[{x}]/td[2]/div[2]/a').click()
    for i in range(2,7):
        sleep(0.3)
        for j in range(1,4):
            sleep(0.3)
            p = browser.find_element(By.XPATH,f'/html/body/div[5]/main/div[2]/div/div/div/form/div[{i}]/p[{j}]/input')
            val = p.get_attribute('value')
            if val == '1':
                sleep(0.5)
                browser.execute_script("arguments[0].click();",p)
    sleep(5)
    
    try:
        alert = browser.switch_to.alert

         # print hello if alert is present
 

        # close the alert box
        alert.accept()
        sleep(1)
    except NoAlertPresentException:
    # print nothing if no alert is present
        pass
    browser.find_element(By.XPATH,f'/html/body/div[5]/main/div[2]/div/div/div/p/input').click()
  






for x in range(1,6):
    sleep(1)

    browser.find_element(By.XPATH,f'/html/body/div[5]/main/div[2]/div[2]/section[3]/div[2]/div/div/div/table/tbody/tr[{x}]/td[2]/div[2]/a').click()
    for i in range(2,5):
        sleep(1)
        for j in range(1,4):
            sleep(1)
            p = browser.find_element(By.XPATH,f'/html/body/div[5]/main/div[2]/div/div/div/form/div[{i}]/p[{j}]/input')
            val = p.get_attribute('value')
            if val == '1':
                sleep(1)
                browser.execute_script("arguments[0].click();",p)
    sleep(6)
    
    try:
        alert = browser.switch_to.alert

         # print hello if alert is present
        print("hello")

        # close the alert box
        alert.accept()
        sleep(1)
    except NoAlertPresentException:
    # print nothing if no alert is present
        pass
    browser.find_element(By.XPATH,f'/html/body/div[5]/main/div[2]/div/div/div/p/input').click()
    
sleep(200)





#//*[@id="col-1165167830"]/div/table/tbody/tr[1]/td[2]/div[2]/a
#/html/body/div[5]/main/div[2]/div[2]/section[2]/div[2]/div/div/div/table/tbody/tr[4]/td[2]/div[2]/a
#/html/body/div[5]/main/div[2]/div[2]/section[2]/div[2]/div/div/div/table/tbody/tr[5]/td[2]/div[2]/a
#
#/html/body/div[5]/main/div[2]/div[2]/section[3]/div[2]/div/div/div/table/tbody/tr[1]/td[2]/div[2]/a


#/html/body/div[5]/main/div[2]/div/div/div/form/div[2]/p[1]/input
#/html/body/div[5]/main/div[2]/div/div/div/form/div[2]/p[2]/input
#/html/body/div[5]/main/div[2]/div/div/div/form/div[3]/p[1]/input
#/html/body/div[5]/main/div[2]/div/div/div/form/div[3]/p[2]/input
#/html/body/div[5]/main/div[2]/div/div/div/form/div[4]/p[1]/input
#/html/body/div[5]/main/div[2]/div[2]/section[1]/div[2]/div/div/div/table/tbody/tr[1]/td[2]/div[2]/a
#/html/body/div[5]/main/div[2]/div[2]/section[1]/div[2]/div/div/div/table/tbody/tr[2]/td[2]/div[2]/a




#/html/body/div[5]/main/div[2]/div/div/div/form/div[2]/p[1]/input
#/html/body/div[5]/main/div[2]/div/div/div/form/div[2]/p[1]/input



