import csv
# encoding='utf-8-sig'로 '/ufeff' 제거
fin = open('../대구기온2.csv', 'r', encoding='utf-8-sig')       # 읽기용으로 파일 open
data = csv.reader(fin, delimiter=',')

# newline'' : 1 라인씩 건너 뛰며 저장되는 현상 없앰
fout = open('../대구기온2-utf8.csv', 'w', newline='', encoding='utf-8-sig')       # 쓰기용으로 파일 open
wr = csv.writer(fout)       # 저장

for row in data:
    for i in range(len(row)):
        row[i] = row[i].replace('\t','')        # '/t' 제거
        # if row[0] == '1959-08-15':
        #     print(row)
    print(row)
    wr.writerow(row)    # writerow(row): 한 행씩 파일로 저정

fin.close()
fout.close()
print('파일 저장 완료')
