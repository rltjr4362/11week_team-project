import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://coronaboard.kr/'

driver = webdriver.Chrome('C:/Users/82102/Desktop/first_git_project/team-project/chromedriver.exe')
driver.get(url) # url 불러오기
driver.implicitly_wait(3) # 3초 기다리기

data = driver.page_source # 페이지 소스 가져오기

soup = BeautifulSoup(data, 'html.parser')

soup_select=soup.select('#country-table > div > div > table') #테이블 가져오기
print(soup_select)
df = pd.read_html(soup_select.prettify())[0]

print(type(df))

print(df)

driver.quit()

a=input('국가를 입력하세요: ')
for i in range(75):
    if a in df.iloc[i,1]:
        nation=i
        break
list=[]
c=''
for i in range(2,5):
    b=df.iloc[nation,i].split()[0]
    c+=' '+b
c=c.replace(',','').split()
c = [int(i) for i in c]

print(c)