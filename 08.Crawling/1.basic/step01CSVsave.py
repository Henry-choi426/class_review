# 데이터를 csv로 저장하기
# 실습 단계 1 - join()
#               반복해서 보유한 데이터들을 하나씩 가공 가능
# 실습 단계 2 - csv 모듈 사용
'''
#step01 '''
print('no,name,age')

# list의 데이터로 csv 구조로 변환
print(",".join(['1', '허준', '60']))  #1,허준,60
print(",".join(['2', '신사임당', '80']))


#step02 - csv 모듈 사용
'''
    history.csv 라는 파일에 쓰기
    csv 포멧 작성후에 new line 반영
    한글 데이터가 보유 고려
    
    한번에 하나의 row만 출력? 1차원 list
    한번에 다수의 row들 출력? 2차원 list 구성

'''

#모듈 import
import csv

with open("history.csv", "w", newline='', encoding="utf-8-sig") as f:
    #history.csv 파일로 csv 작성 가능한 객체화
    #writer 변수로 호출하는 함수는 csv 파일로 작성 가능한 기능
    writer = csv.writer(f)

    #csv 파일의 header 작성
    writer.writerow(['no','name','age'])
    writer.writerows([['1', '허준', '60'],
                      ['2', '율곡', '600'],
                      ['3', '이산', '10'] ])
   