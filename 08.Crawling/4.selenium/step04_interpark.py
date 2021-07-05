from selenium import webdriver
from bs4 import BeautifulSoup
import time

# step01 : 네이버에 실행 후  AI 키워드로 검색
driver = webdriver.Chrome("c:/driver/chromedriver")
driver.get("http://tour.interpark.com/?mbn=tour&mln=tour_tour")

#tag 검색

search_box = driver.find_element_by_xpath('//*[@id="SearchGNBText"]')

#검색한 input tag의 내용 수정
search_box.clear()  # 혹시 내용이 있으면 삭제

#input  tag에 데이터 입력
search_box.send_keys("파리")  # 입력

#전송 버튼 클릭 
btn = driver.find_element_by_xpath('//*[@id="dHead"]/div[2]/div[1]/form/fieldset/button[1]')
btn.click()

time.sleep(1) 
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser',)
# ----------
for i in soup.find(class_='oTravelBox').find_all("li",class_="boxItem"):

    print('상품명 = ' + i.find('h5', class_="proTit").string)
    print('코멘트 = ' + i.find('p', class_="proSub").string)
    print("가격=",i.select('div > .proPrice')[0].get_text().replace(" ","").replace("\n",""))
    print(i.select('div > .proInfo')[0].get_text().replace(" ","").replace("\n",""))
    print(i.select('div > .proInfo')[2].get_text().replace(" ","").replace("\n",""))

time.sleep(1) 
driver.quit()

