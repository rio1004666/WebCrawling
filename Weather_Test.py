
import os
from selenium import webdriver
import time
from datetime import datetime
want_date = input('원하는 날짜를 입력해주세요')
browser = webdriver.Chrome('./chromedriver.exe')
browser.get('https://www.weather.go.kr/w/obs-climate/land/city-obs.do')

input_date = browser.find_element_by_css_selector('#select-tm')
elem = browser.find_element_by_id('select-tm').clear()
time.sleep(1)
input_date.send_keys(want_date)
search_btn = browser.find_element_by_css_selector('#default-form > div:nth-child(4) > div.cmp-form-input.cmp-form-input-tripple.label-on > input[type=submit]:nth-child(3)')
search_btn.click()
cities = browser.find_elements_by_css_selector('#weather_table > tbody > tr')

temp_list = want_date.split('.') # 문자열을 .으로 쪼개서 리스트에 저장
temp2_list = temp_list[-1].split(':') # 맨마지막에 있는 것은 : 이므로 다시 쪼개서 저장

directory = "./weather/{:%Y-%m-%d}".format(datetime.now())

if not os.path.exists(directory):
    os.makedirs(directory)

fname = "{}-{}-{}-{}-{}.cvs".format(temp_list[0],temp_list[1],temp_list[2],temp2_list[0],temp2_list[1])
file = open(directory + '/'+ 'Weather_' + fname, 'w', encoding='utf-8')



for city in cities:
    print(city.text)
    file.write('%s\n' % (city.text))

file.close()
print('데이터 수집 완료...')