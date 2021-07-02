#step01robotsParser.py
'''
[1] 용어
    1. parser
        - 구문해석 -> 문법 검증 -> 변환 의 과정

[2]  robots.txt 용도
    각 사이트별 크롤링 허용 범위를 표현하는 파일
    법적인 효력(?)은 있지만 기술적으론 이 파일만으로 불가 

-------------
[1] 핵심
robots.txt 파일을 파싱해서 해당 사이트 크롤링 가능 여부 확인 하기
wikibook.co.kr : 크롤링 가능
    http://wikibook.co.kr/robots.txt
google.co.kr : 크롤링 불허
naver.com : 오류

[2] 개요
1. 크롤링 가능 여부를 소개하는 file 확인 로직
    1. 파일명 : robots.txt
    2. url상에서 직접 확인 명령어 : 
        http://ip:80/robots.txt
        http://domain:80/robots.txt

2. python 관련 library
    urllib 에 robots.txt 확인 가능한 library
        - robotparser의 RobotFileParser 클래스

3. robots.txt의 부연 설명 사이트
    - https://extrememanual.net/10728
'''

# 파이썬 표준 library
import urllib.robotparser

# robots.txt 파일을 위한 RobotFileParser 클래스
rp = urllib.robotparser.RobotFileParser()

# 해당 사이트 크로링 해도 되는지 확인

# http://wikibook.co.kr/ 사이트 크롤링 가능 여부 확인
rp.set_url("http://wikibook.co.kr/robots.txt")

# robots.txt 파일 read
rp.read()

# wikibook.co.kr 사이트 크롤링 여부 확인
data = rp.can_fetch("mybot", "http://wikibook.co.kr/") # 검증해주는 애 한테 단순히 이름을 부여한 것
print(data)  # False



rp.set_url("http://www.google.com/robots.txt")
rp.read()
data = rp.can_fetch("mybot", "http://www.google.com")
print(data)   # False



rp.set_url("http://www.naver.com/robots.txt")
rp.read()
data = rp.can_fetch("mybot", "http://www.naver.com")
print(data)
