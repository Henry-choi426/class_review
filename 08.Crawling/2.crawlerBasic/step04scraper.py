''' step05_scraper.py
1. 주제
    한빛 미디어의 책 list page에서 각각의 list의 link 정보 추출해서 개별 상세 page의 url값 스크래핑 하기

2. 활용 사이트
    http://www.hanbit.co.kr/store/books/full_book_list.html
    한빛 -> Store -> 전체 목록

3. 의도 및 구현 방식
    1. 파이썬으로 스크래핑 흐름 이해하기
        - 전체도서목록 page -> 각 도서별 링크 정보 스크래핑 해서 -> DB에 데이터 저장하기
        - 실행후 books.db가 존재하는 경로인 이 python예제가 실행된 경로내에서 검색
            >sqlite3 books.db
            sqlite>select * from books;
        

    2. 스크래핑 해서 DataBase에 저장되는 정보
    1. 리스트의 도서명(title)
    2. 도서명의 하이퍼링크 url 값
    
    3. process
        3-1. 웹페이지 추출하기 : fetch()
        3-2. 스크래핑 하기 : scrape()
        3-3. db에 데이터를 저장하기 : save()

    4. 구현 함수 상세 내용
        - 각 기능을 함수로 처리 
        4-1. 웹페이지 추출하기 : fetch(url)
            : 매개 변수로 url을 받고 지정한 url의 웹 페이지를 추출

        4-2. 필요한 정보만 스크래핑 하기 : scrape(html)
            : 매개변수로 html을 받고, 정규 표현식을 사용해 HTML에서 도서 정보 추출

        4-3. 데이터를 RDBMS에 저장하기 : save(data)
        : 매개변수로 저장할 정보를 받고, Oracld DB 에 저장
'''

import re
from urllib.request import urlopen
from html import unescape

import cx_Oracle
import os


#로직 - 완성
def main():
    """
    호출 순서
        fetch(), scrape(), save() 순으로 호출
    """
    html = fetch('http://www.hanbit.co.kr/store/books/full_book_list.html')
    # print(html)
    books = scrape(html)
    save(books)


# 완성
# 웹페이지 추출하기 : fetch()
# 웹 페이지 인코딩 형식은 추출한 인코딩 정보를 기반으로 추출
def fetch(url):  
    f = urlopen(url)
    
    # HTTP 헤더를 기반으로 인코딩 형식을 추출
    encoding = f.info().get_content_charset(failobj="utf-8")
    print("--- 1. 인코딩 정보 : ", encoding)
    
    # 추출한 인코딩 형식을 기반으로 문자열을 디코딩, 정보로 디코딩 안 할 경우 한글 깨짐 발생 가능.
    html = f.read().decode(encoding)

    #print("--- 2. 모든 문서 내용 추출 ", html)
    return html

    

#로직 - 미완성
# 필요한 정보만 스크래핑 하기 : scrape()
'''
추출할 데이터 일부 예시
url : http://www.hanbit.co.kr/store/books/look.php?p_code=B7198274060
title :  재미있고 빠른 한글 1권 : 기본 모음과 자음
'''
def scrape(html):
    """
    매개변수 html로 받은 HTML 문서의 내용을 정규 표현식을 사용해서 도서 정보를 추출
    반환값: 도서(dict) 리스트
    """

    books = []

    # title과 link 착출
    for data in re.findall(r'<td class="left"><a href=.*?</td>', html):
        href = re.search(r'href="(.*?)(")',data).group(1)
        # https://www.hanbit.co.kr/store/books/look.php?p_code=B7468885216
        url = 'https://www.hanbit.co.kr' + href

        title = d2 = re.sub("<.*?>", "", data)

        books.append({'url':url,'title':title})
    return books


# <td class="left"><a href="/store/books/look.php?p_code=B9602652686">데이터 스토리</a></td>

#로직 - 미완성
# 데이터를 RDBMS에 저장하기 - books table에 저장하기
def save(books):
    # 접속
    con = cx_Oracle.connect("SCOTT/TIGER@localhost:1521/xe")
    # 커서를 추출
    cur = con.cursor()
    cur.execute('''DROP TABLE books''')
    # books 테이블을 생성 - 
    cur.execute('''
        CREATE TABLE books (
            title varchar2(200),
            url varchar2(200)
        )
    ''')
    # executemany() 메서드를 사용하면 매개변수로 리스트를 지정할 수 있음
    cur.executemany('INSERT INTO books VALUES (:title, :url)', books)
    con.commit()
    cur.close()
    con.close()

if __name__ == '__main__':
    main()