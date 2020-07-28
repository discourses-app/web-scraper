from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Safari()

url = "https://sa.ucla.edu/ro/public/soc"


driver.get(url)
time.sleep(1)
element = driver.find_element_by_id("search_by")
element.click()
ActionChains(driver).move_to_element(element)
select = Select(element)
# select.select_by_index(1)
select.select_by_index(0)

enter_bar = driver.find_element_by_id("select_filter_subject")
enter_bar.click()
enter_bar.clear()
time.sleep(3)
enter_bar.send_keys(" ")
for i in range(0, 30):
    enter_bar.send_keys(Keys.BACKSPACE)
# for i in range (0,30):
enter_bar.send_keys(Keys.ARROW_DOWN)
time.sleep(1)
enter_bar.send_keys(Keys.ENTER)
time.sleep(2)
enter_bar.send_keys(Keys.ENTER)
time.sleep(7)
expand = driver.find_element_by_id("expandAll")
ActionChains(driver).move_to_element(expand)
javaScript = "document.getElementById('expandAll').click();"
driver.execute_script(javaScript)
expand = driver.find_element_by_id("expandAll")
ActionChains(driver).move_to_element(expand)
time.sleep(5)
classTitle = str(driver.execute_script("return document.getElementById('spanSearchResultsHeader').textContent;"))
classTitle = classTitle.split('(')
classTitle = classTitle[1].split(')')
className = classTitle[0]
allResults = driver.execute_script("return document.getElementsByClassName('row-fluid class-title');")
for Class in allResults:
    ClassSub = Class.get_attribute("id")
    children = str(ClassSub)+"-children"
    titleID = str(ClassSub) + "-title"
    classSubtext = (driver.find_element_by_id(titleID)).text.split(" ")
    print (className + " " + classSubtext[0])
    javascript = "return (document.getElementById('" + str(children) +"')).children;"
    firstChild = driver.execute_script(javascript)
    for child in firstChild:
        id = child.get_attribute("id")
        javascript = "return document.getElementById('" + str(id) + "').children;"
        results = driver.execute_script(javascript)
        for cols in results:
            name = cols.get_attribute("class")
            if (name == "sectionColumn"):
                section = cols.text.strip().split(" ")
                tempNum = (str(section[0]) + " " + str(section[1])).split("\n")
                sectionNum = tempNum[0]
                print(sectionNum)
            if (name == "instructorColumn hide-small"):
                print(cols.text.strip())


print("The number of classes are " + str(len(allResults)))
classTitle = str(driver.execute_script("return document.getElementById('spanSearchResultsHeader').textContent;"))
classTitle = classTitle.split('(')
classTitle = classTitle[1].split(')')
className = classTitle[0]
print(className)
