import pandas as pd
import matplotlib as mpl
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://coronaboard.kr'

driver = webdriver.Chrome('C:/Users/82102/Desktop/first_git_project/team-project/chromedriver.exe')
driver.get(url) # url 불러오기
driver.implicitly_wait(3) # 3초 기다리기

data = driver.page_source # 페이지 소스 가져오기


