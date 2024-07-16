from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from time import sleep

# Function to initialize the browser
def init_browser(driver_path):
    browser = webdriver.Chrome(driver_path)
    browser.maximize_window()
    return browser

# Function to login
def login(browser, username, password):
    browser.get('https://www.educazionedigitale.it/goccedisostenibilita/moduli-formativi/')
    sleep(1)
    # Reject cookie
    browser.find_element(By.XPATH, '/html/body/div[3]/div/div/div/div[2]/button[3]').click()
    # Open login form
    browser.find_element(By.XPATH, '/html/body/div[5]/header/div/div[2]/div[1]/div[4]/ul/li[5]/a').click()
    sleep(0.3)
    # Enter credentials and login
    browser.find_element(By.ID, 'user').send_keys(username)
    sleep(0.1)
    browser.find_element(By.ID, 'pass').send_keys(password)
    sleep(0.1)
    browser.find_element(By.NAME, 'invia').submit()
    sleep(0.3)
    # Handle potential second login form
    try:
        browser.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div/form/input[2]').click()
        sleep(0.3)
        browser.find_element(By.NAME, 'invia').submit()
    except:
        pass

# Function to handle form questions
def handle_form_questions(browser, section_xpath):
    for i in range(2, 7):
        sleep(0.3)
        for j in range(1, 4):
            sleep(0.3)
            p = browser.find_element(By.XPATH, f'{section_xpath}/form/div[{i}]/p[{j}]/input')
            val = p.get_attribute('value')
            if val == '1':
                sleep(0.5)
                browser.execute_script("arguments[0].click();", p)

# Function to handle sections
def handle_section(browser, section_number, sub_section_count, row_count):
    for x in range(1, row_count + 1):
        sleep(0.3)
        section_xpath = f'/html/body/div[5]/main/div[2]/div[2]/section[{section_number}]/div[2]/div/div/div/table/tbody/tr[{x}]/td[2]/div[2]/a'
        browser.find_element(By.XPATH, section_xpath).click()
        handle_form_questions(browser, '/html/body/div[5]/main/div[2]/div/div/div')
        sleep(4)
        try:
            alert = browser.switch_to.alert
            print("hello")
            alert.accept()
            sleep(1)
        except NoAlertPresentException:
            pass
        browser.find_element(By.XPATH, '/html/body/div[5]/main/div[2]/div/div/div/p/input').click()

# Main script
if __name__ == "__main__":
    driver_path = '/Users/francesco/Downloads/chromedriver_mac_arm64/chromedriver'
    browser = init_browser(driver_path)
    login(browser, 'stu-9148302-04', 'i2h0z5')
    
    # Handling sections
    handle_section(browser, 1, 4, 10)
    handle_section(browser, 2, 7, 10)
    handle_section(browser, 3, 5, 6)

    sleep(200)
    browser.quit()
