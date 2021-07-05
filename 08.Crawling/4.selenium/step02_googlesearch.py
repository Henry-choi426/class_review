from selenium import webdriver
import time

# step01 : 네이버에 실행 후  AI 키워드로 검색
driver = webdriver.Chrome("c:/driver/chromedriver")
driver.get("https://www.google.com/")

#tag 검색
'''
해당 name 찾은 것
<input id="query" name="query" type="text" title="검색어 입력" maxlength="255" class="input_text" 
tabindex="1" accesskey="s" style="ime-mode:active;" autocomplete="off" placeholder="검색어를 입력해 주세요." 
onclick="document.getElementById('fbm').value=1;" value="" data-atcmp-element="">
'''
tag = driver.find_element_by_name('q')

#검색한 input tag의 내용 수정
tag.clear()  # 혹시 내용이 있으면 삭제

#input  tag에 데이터 입력
tag.send_keys("AI")  # 입력

#전송 버튼 클릭 
tag.submit()
time.sleep(5) 
driver.quit()