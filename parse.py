from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_ajax(driver):
    wait = WebDriverWait(driver, 6000)
    try:
        wait.until(lambda driver: driver.execute_script('return jQuery.active') == 0)
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    except Exception as e:
        pass


driver = webdriver.Chrome()

driver.get("http://spys.one/free-proxy-list/CN/")
wait_for_ajax(driver)

table = driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[5]/td/table")

trList = table.find_elements_by_tag_name("tr")

title = trList.__getitem__(2)
print(title.text)

for i in range(3, trList.__len__()):
    print(trList.__getitem__(i).text)
driver.close()
