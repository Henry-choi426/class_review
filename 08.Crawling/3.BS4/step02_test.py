from bs4 import BeautifulSoup
html = '''<!DOCTYPE html>
<html lang="ko">
<body>
  <div id="main-goods" role="page">
      <h1>과일과 야채</h1>

      <ul id="fr-list">
        <li class="red green" data-lo="ko">사과</li>
        <li class="purple" data-lo="us">포도</li>
        <li class="yellow" data-lo="us">레몬</li>
        <li class="yellow" data-lo="ko">오렌지</li>
      </ul>

      <ul id="ve-list">
        <li class="white green" data-lo="ko">무</li>
        <li class="red green" data-lo="us">파프리카</li>
        <li class="black" data-lo="ko">가지</li>
        <li class="black" data-lo="us">아보카도</li>
        <li class="white" data-lo="cn">연근</li>
      </ul>

  </div>
<body>
</html>'''

'''
레몬
아보카도
파프리카
아보카도
아보카도
아보카도

문법 : find_all(body명)
        re.compile("^b") -> b로 시작하는 tag들 출력
        ["a", "b"] -> a,b 태그 다 찾기.
        id="link2" -> id가 link2 인 데이터 찾기.
        soup.find(text=re.compile("sisters")) -> text에 sisters를 포함한 태그 출력
        soup.find_all(href=re.compile("elsie"), id='link1') -> 하나 이상의 키워드 인자
        soup.find_all("a", class_="sister") -> a 태그에 class 가 sister 인 놈들


        for tag in soup.find_all(True): True 인 경우 출력
        - 함수 정의하여 데이터 출력
        def has_class_but_no_id(tag):
            return tag.has_key('class') and not tag.has_key('id')
        soup.find_all(has_class_but_no_id) -> 함수 return값이 yes or no로 출력

'''
soup = BeautifulSoup(html, 'html.parser',)

print(soup.find(id='fr-list').select('.yellow')[0].string)
print(soup.find(id='ve-list').select('.black')[1].string)
print(soup.find(id='ve-list').select('.red')[0].string)
print((soup.find(id='ve-list').select('.black')[1].string+'\n') * 3)


# step01 : css 선택자로 데이터 추출하기
# string

# nth-of-type() : parameter 값에 해당하는 순번의 자식
# print(soup.select_one("li:nth-of-type(3)").string)
# 해당 tag의 text를 의미하되, text인 경우에만 데이터 착출
print(soup.select_one("li:nth-of-type(3)").string)              # 레몬

# > : 하위 자식
# 미리 데이터 하나만 select 하기
print(soup.select_one("#ve-list > li:nth-of-type(4)").string)   # 아보카도

# ve-list 하위 li에서 data-lo가 us인 태그들의 list를 가져오고, index가 0인 놈 가져옴
print(soup.select("#ve-list > li[data-lo='us']")[0].string)     # 파프리카

# ve-list 하위 li에서 class가 black인 놈 출력
print(soup.select("#ve-list > li.black")[1].string)             # 아보카도

# step02 : find() 함수로 추출하기
# 하위로 가는것이 아닌 필요한 인자들을 줌으로써 한번에 찾음
attDatas = {"data-lo":"us", "class":"black"}
print(soup.find("li", attDatas).string) # 아보카도

# step03 : find() 함수로 연속적으로 추출하기
# 하위로 데이터를 연속 find함수를 사용하여 출력
print(soup.find(id="ve-list").find("li", attDatas).string)  #아보카도