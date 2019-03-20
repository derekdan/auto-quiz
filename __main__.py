# -*- coding:utf-8 -*-

import sys
from timu import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

reload(sys)
sys.setdefaultencoding('utf-8')

browser = webdriver.Firefox()
browser.set_window_size(400,750)
url = sys.argv[1]
browser.get(url)

time.sleep(5)

try:
#browser.get("http://api.yiqiapp.cn/dkdtweb/?user_name=15710895071&pd=4570f5f0388498920b1d79f62bca21c1&type=pc&sign=3c1b3f9d26e8b64952e2defe926b05f2&mobile=0")
	wait = WebDriverWait(browser,80)
	try:
		button = browser.find_element_by_css_selector('.btn')
		button.click()
	except:
		pass
	game_value = browser.find_element_by_css_selector('.games .value').text
	if game_value.decode('utf-8') in ('0', '-'):
		print 0
	else:
		print 1
	time.sleep(2)
	button = browser.find_element_by_css_selector('.with-computer')
#button = browser.find_element_by_css_selector('.with-player')
	button.click()
	time.sleep(2)
	button = browser.find_element_by_css_selector('.btn-begin')
	button.click()
	time.sleep(3)
	for timer in xrange(5):
		text = str(timer+1)
		title = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.title'), text))
		time.sleep(1)
		topic = browser.find_element_by_css_selector('.topic').text
		time.sleep(1.5)
		cell = browser.find_elements_by_css_selector('.cell')
		ncell = len(cell)
		cell_btn = cell[0]
#	cell_btn = browser.find_element_by_css_selector('.cell:first-child')
		for x in timu:
			if x[0] == topic.decode('utf-8'):
				for j in xrange(ncell):
					if cell[j].text.decode('utf-8') == x[1]:
#					cell_btn = browser.find_element_by_css_selector('.cell:nth-child(%d)'%(j+1))
						cell_btn = cell[j]
		cell_btn.click()
#	time.sleep(5)
	time.sleep(15)
except:
#print 1
	pass
browser.close()
