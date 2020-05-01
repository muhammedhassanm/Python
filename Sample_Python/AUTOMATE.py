# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 17:59:18 2020

@author: Muhammed Hassan M
"""

from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")
#chrome_options.add_argument("--headless")
#chrome_options.add_argument("--disable-notifications")
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--verbose')
chrome_options.add_experimental_option("prefs", {
        "download.default_directory": "C:/Users/Muhammed Hassan M/Desktop/OIl&GAS/data/PDF",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing_for_trusted_sources_enabled": False,
        "safebrowsing.enabled": False
})
#chrome_options.add_argument('--disable-gpu')
#chrome_options.add_argument('--disable-software-rasterizer')
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:/chromedriver.exe')
url = "https://rrcsearch3.neubus.com/esd3-rrc/index.php?_module_=esd&_action_=keysearch&profile=15"
driver.get(url)

#inputElementdistrict = driver.find_element_by_xpath("//*[@id='districtDROPDOWN']").click()
ddelement= Select(driver.find_element_by_id('districtDROPDOWN'))
ddelement.select_by_value('01')
search_button = driver.find_elements_by_xpath('//*[@id="docSearchButton"]')[0]
search_button.click()
mytable = driver.find_element_by_xpath('//*[@id="searchResults"]/tbody/tr').size()

for row in mytable.find_elements_by_css_selector('tr'):
    for cell in row.find_elements_by_tag_name('td'):
        print(cell.text)

