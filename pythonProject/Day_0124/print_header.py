import csv


f=open('../대구기온2-utf8.csv', encoding='utf-8-sig')
data=csv.reader(f, delimiter=',')
header = next(data)         # next는 내용을 읽으며 다음 행으로 이동
print(header)
           # 헤더 문자열 출력

i=1
for row in data:
    print(row)
    if i >= 5:
        break           # 5개의 데이터를 출력하면 break
    i += 1

f.close()