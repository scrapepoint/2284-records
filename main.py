from selenium import webdriver
import csv
import time
driver = webdriver.Chrome(executable_path="chromedriver")

with open('Data.csv', 'w', newline='', encoding="utf-8") as new:
    fields = ['Name', 'ID', 'Preferred Address City', 'Preferred Address State Code']
    writer = csv.writer(new)
    writer.writerow(fields)

driver.get("https://customer28911c419.portal.membersuite.com/profile/CreateAccount_CreateUser.aspx")
driver.find_element_by_id("ddlOrganization_Arrow").click()
time.sleep(2)
current = driver.find_element_by_xpath('//div[@id="ddlOrganization_MoreResultsBox"]/span').text
while current != "Showing 1-2,284 out of 2284":
    driver.find_element_by_xpath('//div[@id="ddlOrganization_MoreResultsBox"]').click()
    time.sleep(2)
    current = driver.find_element_by_xpath('//div[@id="ddlOrganization_MoreResultsBox"]/span').text
    print(f'Loading: {current}')
rows = driver.find_elements_by_xpath('//li[@class="rcbItem  rcbTemplate"]')
for row in rows:
    cols = row.find_elements_by_xpath('.//td')
    data = []
    for i in range(len(cols)):
        if i % 2 == 0:
            data.append(cols[i].text)
    print(data)
    print("---------------------------------------")
    with open('Data.csv', 'a', newline='', encoding="utf-8") as new:
        writer = csv.writer(new)
        writer.writerow(data)
driver.close()
