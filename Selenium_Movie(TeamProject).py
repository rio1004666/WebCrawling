

from selenium import webdriver
from datetime import datetime
import logging

browser = webdriver.Chrome('./chromedriver.exe')
browser.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt')
browser.find_element_by_css_selector('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')