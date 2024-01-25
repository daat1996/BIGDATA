import csv


f = open('subwayfee.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)
max_rate= 0
rate = 0

# for row in data:
#     for i in range(4,8):
#         row[i] = int(row[i])        # 4,5,6,7 컬럼값을 정수로 변환
#     rate = row[4] / row[6]          # [6]컬럼의 값이 0인 행 확인 용도
#     if rate > max_rate:
#         max_rate=rate
# print(max_rate)
# 에러발생  => 무임승차(row[6])컬럼에 0이 존재함


for row in data:
    for i in range(4, 8):
        row[i] = int(row[i])    #4,5,6,7 컬럼값을 정수로 변환
    rate = row[4] / (row[4]+ row[6])
    if row[6] == 0:             # 무임승차 인원[6]이 없는 역 출력
        print(row)




f.close()

