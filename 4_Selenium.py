"""
날짜: 2021/08/31
이름: 강병화
내용: 파이썬 Selenium(가상브라우저) 패키지 실습
"""

from selenium import webdriver  # 외부 패키지이므로 설치해야한다 file => settings => python interpreter
# 가상 브라우저 실행

browser = webdriver.Chrome('./chromedriver.exe') # 크롭 드라이버를 다운받는다 여기에 둔다

# 네이버 이동

browser.get('http://naver.com')

# 로그인 버튼 클릭
login_a = browser.find_element_by_css_selector('#account > a') # 로그인버튼 선택자
login_a.click()

# 아이디, 비번 입력

input_id = browser.find_element_by_css_selector('#id')
input_pw = browser.find_element_by_css_selector('#pw')

input_id.send_keys('abcd')
input_pw.send_keys('1qw2e435')

# 로그인 버튼 클릭

button_login = browser.find_element_by_css_selector('#log\.login')
button_login.click()