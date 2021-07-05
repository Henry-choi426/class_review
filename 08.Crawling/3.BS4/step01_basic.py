# html의 필수 표현법
'''
1. html 문서의 tree구조로 특정 tag및 text data 찾아가는 형식은 dom 기반
2. dom
    - Document Object Model
    - html 모든 요소(tag, 속성, text..)를 객체로 관리
    - 실시간 가변적인 동적 화면 구성에 필수 핵심 기술
    - 화면을 변경시키는 기술셋
    - 스펙 : w2c에서 제시, 이 dom 기술을 지원하는 개발 언어들은 모든 언어가 지원
    - 수업시간엔 JS 기반의 dom 처리를 학습
    - id로 특정 tag 검색 : document.GetElementByID("아이디명")
    - next_sibling : 현 위치상에서 다음 형제 검색
    - 해킹 시 필수 기술

    . : class 속성
    # : id 속성
    이름 : tag명 의미 표기
'''

html='''
<html>
    <body>
        <h1>스크래핑이란?</h1>
        <h1>담배란?</h1>
        <p id="one">웹페이지 1</p>
        <p id="two">웹페이지 2</p>
        <span class="redColor">
            <p>웹페이지3</p>
        </span>
        <ul>
            <li><a href="www.daum.net">다음</a></li>
            <li><a href="www.naver.com">네이버</a></li>
        </ul>        
    </body>
</html>
'''
# bs4 - html 문서를 tag, 속성, css 등으로 섬세하게 관리 가능한 API
from bs4 import BeautifulSoup
# 크롤링 대상의 데이터와 구문해석, 문법체크, 변환 가능한 parser 설정
soup = BeautifulSoup(html, 'html.parser',)

print('1. 원리'+"*"*50)

print(soup.html.h1) # <h1>스크래핑이란?</h1>
print(type(soup.html.p)) # <class 'bs4.element.Tag'


# html(xml) 문서는 족보구조 , 즉 Tree 구조
# html 상에서 new line(br tag)는 text 로 간주
# next_sibling : 현 위치상에서 다음 내 형제
'''
        <p id="one">웹페이지 1</p>
        <p id="two">웹페이지 2</p>
'''
print(soup.html.p)  # <p id="one">웹페이지 1</p>
print(soup.html.p.next_sibling)  # new line, 즉 test 동생
print(soup.html.p.next_sibling.next_sibling)  # <p id="two">웹페이지 2</p>

print(soup.html.span.p) # <p>웹페이지3</p>

# text 데이터들은 string 속성명과 get_text() 함수로 착출
print(soup.html.span.p.string) # 웹페이지3
print(soup.html.span.p.get_text()) # 웹페이지3


print('2. find 함수'+"*"*50)
print(soup.find(id='one'))  # <p id="one">웹페이지 1</p>
print(soup.find(id='one').string)   # 웹페이지 1

'''
html css 속성은 중복 표현 : 이름을 동일하게 적용햇 공통 ui
.redColor : class 속성이 redColor인 것들을 다 찾음 -> 그러므로 list로 반환

.redColor p
    여백을 기준으로 p는 class 속성값이 RedColor인 Tag의 자식인 p tag
    따라서 list 타입으로 반환
'''
print(soup.select('.redColor')) # [<span class="redColor"> <p>웹페이지3</p> </span>]
print(soup.select('.redColor')[0])  # <span class="redColor"> <p>웹페이지3</p> </span>
print(soup.select('.redColor p')[0])    # <p>웹페이지3</p>
print(soup.select('.redColor p')[0].string)    # 웹페이지3

