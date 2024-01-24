import matplotlib.pyplot as plt
import koreanize_matplotlib
import csv


f =open('../대구기온2.csv', 'r', encoding='utf-8')
data = csv.reader(f, delimiter=',')             # delimiter : 구분자(',') csv 파일은 delimiter 생략 가능
print(data)           # csv_reader 객체 출력
count=0
for row in data:                # 대구기온2.csv 파일 전체에 객체 => 1라인씩 읽어옴
    if count > 5:               # 별도의 read()함수 없이 읽어옴 => for 문으로 1줄씩 읽어옴
        break
    else:
        print(row)              # 1 라인 출력
    count += 1




f.close()               # 파일 닫기

