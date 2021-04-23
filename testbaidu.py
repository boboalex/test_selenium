import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome('/Users/bo.zhang/Documents/scripts/TestDataset/app/tool/chromedriver')
driver.get('https://www.baidu.com')

driver.set_window_size(1530, 930)

print(driver.title)
start_time = time.time()
try:
    WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "myDynamicElement")))
except:
    end_time = time.time()
    print(end_time - start_time)
# set_element = driver.find_element(By.CSS_SELECTOR, ".s-isindex-wrap .s-top-right-text")
#
# ActionChains(driver).move_to_element(set_element).perform()

# driver.find_element(By.CSS_SELECTOR, "[id=s-user-setting-menu] .setpref").click()


# time.sleep(20)

# if __name__ == '__main__':
#     pytest.main("-s", "testbaidu.py")