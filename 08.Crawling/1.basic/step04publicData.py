'''
1. 모든 지역에 거주하는 대상 가구수의 합
2. 가구당 평균 전력사용량의 총 평균
3. 가구당 평균 전기요금의 합
'''
import csv

# 각 Columns별 데이터 저장할 list 생성
newhouse = [] #대상 가구수(호)
newVolt = [] #가구당 평균 전력사용량(kWh)
newPay = [] #가구당 평균 전기요금(원)

with open("지역별_전기요금_정보_2021.05_.csv", "r") as f:
    csv_reader = csv.reader(f)
       
    for row in csv_reader:
        print('-', row[1], '-')
        newhouse.append(row[1].strip().replace(",", "")) #index 1 즉 두번째 컬럼값의 데이터 앞뒤 잉여여백 제고 및 제거+
        newVolt.append(row[2].strip().replace(",", ""))
        newPay.append(row[3].strip().replace(",", ""))

# 입력받은 데이터를 for문을 돌려 데이터 합치기.
def sum(sumList):
    sum = 0
    for i in range(1, len(sumList)):
        if(sumList[i] != ""):
            sum = sum + int(sumList[i])
        else:
            pass
    return sum


def avg(avgObject):
    count = 0
    for i in range(1, len(avgObject)):
        if(avgObject[i] != ""):
            count += 1
    
    return (sum(avgObject)/count)

print(sum(newhouse)) 
print(sum(newPay))
print(avg(newVolt))

'''
14882047
565472
335.1764705882353
'''    