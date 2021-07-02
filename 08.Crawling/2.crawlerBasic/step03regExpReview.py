'''
1. step04scraper.py 예제 이해를 위한 도우미 프로그램
2. 정규 표현식 이해하기
'''

import re

def review():   
    # test data - http://www.hanbit.co.kr 에서 발췌한 tag 구조
    data = '<td class="left"><a href="/store/books/look.php?p_code=B7198274060">book info</a></td>'
    
    d1 = re.search(r'<a href="(.*)">', data).group()
    # print(data)
    print("1 --- " + d1 ) #<a href="/store/books/look.php?p_code=B7198274060"> 

    #data 변수의 데이터에서 book_info만 뽑아내기
    # <..> tag 형식의 모든 문자열을 "" length가 0인 문자열로 치환하기
    # . -> 무조건 하나의 문자가 있어야 함
    # * -> 문자열이 있을수도 없을수도 있음
    # ? -> 문자가 없거나 하나이거나
    # d2 = re.sub("<.*?>", "", data)  
    d2 = re.sub("<[^>]+>", "", data)  
    print(d2)


    d2 = re.sub("-", "", "test-test-test")

    print("2 --- " + d2) # book info

    #B7198274060 만 뽑아내기
    # p_code=B7198274060" 를 p_code=으로 시작하는 첫번째 그룹 : B7198274060, 두번째 그룹 : " 으로 구분 후에 group(1) 로 해당 데이터 뽑기
    d3 = re.search(r'p_code=(.*)(")', data).group()
    print("3 --- " + d3)  # p_code=B7198274060"
    print("4 --- " + re.search(r'p_code=(.*)(")', data).group(1)) # B7198274060
    print("5 --- " + re.search(r'p_code=(.*)(")', data).group(2)) # " 
      
    

#최상위 스크립트 환경
if __name__=="__main__":   
    review()

  