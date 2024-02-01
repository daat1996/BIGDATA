import csv

f= open('age.csv', encoding='utf-8-sig')
data = csv.reader(f)

header = next(data)

# print(header)

result=[]
# row[0]: 행정기관
for row in data:
    if '산격3동' in row[0]:        # '산격3동'이 포함된 자료만 출력
        for data in row[3:]:
            result.append(data)
print(result)
f.close()
