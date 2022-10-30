import time
import os
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument("--log-level=3")
# options.add_argument("user-data-dir=C:\\Users\\User\\AppData\\Local\Google\\Chrome Beta\\User Data\\")
# options.binary_location = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe"


def get_filename():
    f = next(os.walk('results'), (None, None, []))[2]
    f = ''.join(f)
    return f


def upload_video():
    nameofvid = get_filename()

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--profile-directory=Default')
    bot = uc.Chrome(options=options)  # executable_path="chromedriver.exe", chrome_options=options

    bot.get("https://studio.youtube.com")
    time.sleep(3)
    upload_button = bot.find_element(By.XPATH, '//*[@id="upload-icon"]')
    upload_button.click()
    time.sleep(1)

    file_input = bot.find_element(By.XPATH, '//*[@id="content"]/input')
    simp_path = 'results/{}'.format(str(nameofvid))
    abs_path = os.path.abspath(simp_path)
    file_input.send_keys(abs_path)

    time.sleep(7)

    next_button = bot.find_element(By.XPATH, '//*[@id="next-button"]')
    for i in range(3):
        next_button.click()
        time.sleep(1)

    done_button = bot.find_element(By.XPATH, '//*[@id="done-button"]')
    done_button.click()
    time.sleep(5)
    bot.quit()
