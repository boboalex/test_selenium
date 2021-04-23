import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException

driver = webdriver.Chrome('/Users/bo.zhang/Documents/chromedriver')


@pytest.fixture(scope="module")
def open():
    print("打开浏览器，打开百度首页")

    driver.get('https://www.baidu.com')
    yield
    print("执行tear down！")
    print("关闭浏览器")
    time.sleep(5)
    driver.quit()


def test_s1(open):
    print(driver.title)
    driver.implicitly_wait(10)
    element = driver.find_element(By.CSS_SELECTOR, ".s-top-more-btn1")
    # element = WebDriverWait(driver, timeout=5).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, ".s-top-more-btn"))
    # )
    # element = driver.find_element(By.CSS_SELECTOR, ".s-top-more-btn1")
    # assert driver.title == "baidu"
    print("element is: ", element)

def test_s2(open):
    set_element = driver.find_element(By.CSS_SELECTOR, ".s-isindex-wrap .s-top-right-text")

    ActionChains(driver).move_to_element(set_element).perform()

    driver.find_element(By.CSS_SELECTOR, "[id=s-user-setting-menu] .setpref").click()

def test_windows(open):
    new_window_script = 'window.open("https://www.google.com")'
    driver.execute_script(new_window_script)
    driver.switch_to.window(driver.window_handles[1])
    print("first visit baidu handle is:", driver.window_handles[0])
    body_text = driver.find_element(By.CSS_SELECTOR, "body").text
    print(body_text)
    driver.close()
    print("current windows are: ", len(driver.window_handles))
    print("second visit baidu handle is:", driver.window_handles[0])
# if __name__ == '__main__':
#     pytest.main("-s", "test_f1.py")
