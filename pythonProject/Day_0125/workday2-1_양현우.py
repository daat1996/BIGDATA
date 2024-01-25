'''
    공공데이터 과제 #2
    1. 지하철 각 노선별 최대 하차 인원을 막대그래프로 표시하고, 하차인원 출력
        - 출근 시간대 : 07:00~08:59
        - 사용파일 : subwaytime.csv 또는 subway.xls
            - 07:00~07:59 하차: index[11], 08:00~08:59 하차: index[13]
'''

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib
import platform

with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    max_people=[0]*7
    max_station_list=['']*7

    for row in data:
        row[4:] = map(int,row[4:])
        people = row[11]+row[13]
        for i in range(7):
            if str(i+1) == row[1][0]:
                if people > max_people[i]:
                    max_people[i] = people
                    max_station = row[3]
                max_station_list[i]=row[1]+' '+max_station

# print(max_people)               # y축
# print(max_station_list)         # x축

for a in range(len(max_people)):
    b,c = max_station_list[a].split()
    print(f'출근 시간대 {b} 최대 하차역: {c}, 하차인원: {max_people[a]:,}명')

plt.figure(figsize=(7,7))
plt.bar(max_station_list,max_people)
plt.title('출근 시간대 지하철 노선별 최대 하차 인원 및 하차역')
plt.xticks(rotation=80)
plt.show()