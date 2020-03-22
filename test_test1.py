from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import allure
import pytest

def test_listSearch():
	browser = webdriver.Chrome("C:\\ChromeWebDriver\\chromedriver.exe")

	browser.get("https://list.am")
	browser.find_element_by_name("q").send_keys("Avto")
	browser.find_element_by_name("q").send_keys(Keys.ENTER)

	posts = browser.find_elements_by_xpath("//*[@class='dl']/a")

	errRes = []
	for p in posts:
		TXT = p.text
		txt = p.text.split('\n')[0]
		if (("Ավտո" in TXT) or ("AVTO" in txt) or ("Avto" in txt) or ("avto" in txt) or ("meqena" in txt) or ("Meqena" in txt) ) == False:
			errRes.append(str(TXT))
			errRes.append("")
		
	browser.close()

	if errRes != []:
		allure.attach(str("\n".join(errRes)), 
			          name="List of umatched items",
			          attachment_type=allure.attachment_type.TEXT)
		assert False
	else:
		assert True


