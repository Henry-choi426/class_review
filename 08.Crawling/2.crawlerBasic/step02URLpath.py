'''
제공 후 분석 및 이해하기

절대 경로와 상대 경로 url 관리하는 연습
'''

#urllib - package명
#parse - 파일명(모듈명)
#urljoin - parse.py 내부에 내장된 urljoin(절대 URL, 상대 URL) 함수

from urllib.parse import urljoin

base = "http://example.com/html/a.html"

#b.html은 a.html와 같은 폴더에 저장되어 있음

# a.html 대신 b.html로 변환
print(urljoin(base, "b.html")) #http://example.com/html/b.html

# 제공받은 pdf p29~30 : 
# authority : 뒤에 나오는 일반적인 호스트 이름 , 사용자이름 , 비밀번호 , 포트 번호 등을 포함
# /표기가 적용될 경우 authority 부분까지만 유효하게 인식
print(urljoin(base, "/b.html")) #http://example.com/b.html

# ../ : 현 위치상에서 상위 디렉토리 의미
print(urljoin(base, "../b.html")) #http://example.com/b.html

print(urljoin(base, "../img/b.html")) #http://example.com/img/b.html

print(urljoin(base, "../css/cssView.css")) #http://example.com/css/cssView.css

# 문법 오류는 없으나, 논리적으로 부적합. Because 이미 2단계 상위 디렉토리가 존재하지 않음.
print(urljoin(base, "../../css/cssView.css")) #http://example.com/css/cssView.css

print(urljoin(base, "/../../css/cssView.css"))  #http://example.com/css/cssView.css  