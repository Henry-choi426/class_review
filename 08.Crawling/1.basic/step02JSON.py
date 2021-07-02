'''
이기종 간에 호환되는 포멧인 JSON 타입으로 변환하는 작업
NoSQL 형식의 데이터 저장 포맷이 Json

JSON 사용 사유 
    : 값 구분이 명확
    : 기기에 종속적이지 않음
    : 모든 언어가 호화되는 포멧
    : csv보다 더 효율적인 사유?
        고유한 key로 데이터 구분
    : 서버로 부터 대량의 데이터를 client가 JSON 포멧으로 많아서 사용 
    
API
    1. python의 list를 Json 형태(객체)로 변환 : dumps()
    2. json의 데이터를 python의 데이터로 변환 : loads()        

실습단계
    1. 모듈 import
    2. test 데이터 구성
    3. json 객체로 변환

고려사항
    1. 한글 데이터 보호(인코딩)
'''
import json

friends=[{'f1' : 1, 'name' : '김혜경'},
         {'f2' : 2, 'name' : '이이'},
         {'f3' : 3, 'name' : '허준'}]
    
print(friends[2]['name'])  #허준
print(friends)

print("----- 1. list를 JSON 객체 형태의 문자열로 변환해 보기 ------ ")
# ensure_ascii=False 생략시 한글 데이터는 아스키코드로 출력
jsonData = json.dumps(friends, ensure_ascii=False)
print(jsonData) # [{'f1': 1, 'name': '김혜경'}, {'f2': 2, 'name': '이이'}, {'f3': 3, 'name': '허준'}]
print(type(jsonData)) # <class 'str'>

print("----- 2. list를 JSON 객체 형태의 문자열로 변환해 보기 -----  ")
jsonData = json.dumps(friends, ensure_ascii=False, indent=2,)
print(jsonData)


print("----- 3. 타입 비교 ----- ")
print(type(friends))
print(type(jsonData))


print("----- 4. json 확장자 파일로 생성 ----- ")
with open("friends.json", "w", encoding="utf-8") as f:
    #list 데이터를 파일에 json 형태의 문자열로 출력
    json.dump(friends, fp=f, ensure_ascii=False)
   