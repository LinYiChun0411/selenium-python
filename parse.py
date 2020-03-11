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

for i in range(2, len(trList)):
    tdList = trList[i].find_elements_by_css_selector("td[colspan='1']")
    if tdList:
        print(tdList[0].text + "," + tdList[1].text + "," + tdList[2].text + "," + tdList[3].text + "," + tdList[
            4].text + "," + tdList[5].text + "," + tdList[6].text + "," + tdList[7].text + "," + tdList[8].text)

driver.close()
