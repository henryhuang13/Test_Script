#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver



browser = webdriver.Chrome()
browser.get("https://www.bing.com")
browser.find_element_by_id("sb_form_q").send_keys("python")
browser.find_element_by_id("sb_form_go").click()






