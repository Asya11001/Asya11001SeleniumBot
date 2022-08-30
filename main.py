from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from data import phone_number
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--headless")

url = "https://web.telegram.org/z/#1985737506"
# driver = webdriver.Chrome(executable_path="D:\\PycharmProjects\\pythonProject\\pycuwa\\selenium-bot\\chromedriver.exe",
#                           options=chrome_options)
driver = webdriver.Chrome(executable_path="/home/ubuntu/PythonProjects/chromedriverLinux",
                          options=chrome_options)

# element = driver.find_element("xpath", "//div[text()='17:00']")

while True:

    try:
        driver.get(url)
        # sleep(223123)
        print("Getting url:", url)
        sleep(5)

        button_login = driver.find_element("xpath", "//*[@id='auth-qr-form']/div/button[1]")
        print("Button login click, button_login: ", button_login)
        button_login.click()
        sleep(5)

        login_phone_input = driver.find_element("xpath", "//input[@aria-label='Your phone number']")
        print("Login phone input found: ", login_phone_input)
        sleep(5)
        login_phone_input.send_keys(Keys.CONTROL + 'a')
        login_phone_input.send_keys("PHONE_NUMBER")
        sleep(2)
        login_phone_input.send_keys(Keys.CONTROL + 'a')
        login_phone_input.send_keys(phone_number)

        login_phone_input.send_keys(Keys.ENTER)
        sleep(3)

        login_keyCode_input = driver.find_element("xpath", "//input[@aria-label='Code']")
        print("login keyCode input found: ", login_keyCode_input)
        print("WAITING FOR YOUR KEY:\n")
        keyCode = int(input())
        login_keyCode_input.send_keys(keyCode)
        login_keyCode_input.send_keys(Keys.ENTER)

        sleep(3)

        login_password_input = driver.find_element("xpath", "//input[@id='sign-in-password']")

        print("login password input found: ", login_password_input)
        print("WAITING FOR YOUR PASSWORD:\n")
        Password = input()
        login_password_input.send_keys(Password)
        login_password_input.send_keys(Keys.ENTER)
        sleep(3)
        print("STARTING WORKING...")
        sleep(2)
        # h3_wallet = driver.find_element("xpath", "//h3[text()='Wallet']")
        # h3_wallet = driver.find_element("xpath", "//h3[contains(., 'Wallet')]")
        h3_wallet = driver.find_element("xpath",
                                        "/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div/div/div/div[4]")
        # h3_wallet = driver.find_element("xpath", "//svg[@xmlns='http://www.w3.org/2000/svg']")
        print("Wallet bot found:", h3_wallet)
        sleep(2)
        h3_wallet.click()

        sleep(3)
        main_text_input = driver.find_element("xpath", "//div[@id='editable-message-text']")
        print("Main text input found:", main_text_input)
        sleep(1)
        main_text_input.send_keys("/menu")
        main_text_input.send_keys(Keys.ENTER)
        sleep(6)

        array_1 = driver.find_elements("xpath", "//img[@data-path='./img-apple-64/1f4b0.png']/../..")
        print("array_1:\n", array_1)
        array_1[len(array_1) - 1].click()
        array_1[len(array_1) - 1].send_keys(Keys.PAGE_DOWN)

        sleep(5)

        array_2 = driver.find_elements("xpath", "//img[@data-path='./img-apple-64/1f4b3.png']/../..")
        print("array_2:\n", array_2)
        array_2[len(array_2) - 1].click()
        array_2[len(array_2) - 1].send_keys(Keys.PAGE_DOWN)

        sleep(5)

        array_3 = driver.find_elements("xpath", "//span[text()='TON']/..")
        print("array_3:\n", array_3)
        array_3[len(array_3) - 1].click()
        array_3[len(array_3) - 1].send_keys(Keys.PAGE_DOWN)

        sleep(5)

        array_4 = driver.find_elements("xpath", "//span[text()='RUB']/..")
        print("array_4:\n", array_4)
        array_4[len(array_4) - 1].click()
        array_4[len(array_4) - 1].send_keys(Keys.PAGE_DOWN)

        sleep(5)

        array_5 = driver.find_elements("xpath", "//span[text()='25000.0 RUB']/..")
        print("array_5:\n", array_5)
        array_5[len(array_5) - 1].click()
        array_5[len(array_5) - 1].send_keys(Keys.PAGE_DOWN)

        sleep(5)

        array_6 = driver.find_elements("xpath", "//strong[contains(text(),'Покупка')]/..")
        print("array_6:\n", array_6)
        # array_6[len(array_6) - 1].send_keys(Keys.PAGE_DOWN)

        sleep(5)

        string = array_6[len(array_6) - 1].get_attribute('innerHTML')

        array = string.split("data-path=")
        message = array[1]
        print(message)

        driver.find_element("xpath",
                            "/html/body/div[1]/div/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div/div/div/div[5]/div/div[3]").click()

        sleep(5)
        main_text_input = driver.find_element("xpath", "//div[@id='editable-message-text']")
        print("Main text input found:", main_text_input)
        sleep(4)
        main_text_input.send_keys(message)
        sleep(4)
        main_text_input.send_keys(Keys.ENTER)

        sleep(90)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()
