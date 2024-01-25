'''
    공공데이터 과제#2
    2. 지하철 각 노선별 퇴근 시간대 최대 하차 인원을 막대그래프로 표시하고, 하차인원 출력
        - 퇴근 시간대 : 19:00~20:59
        - 사용파일: subwaytime.csv 또는 subway.xls
        - 19:00 ~ 19:59 하차 : index[35], 20:00 ~ 20:59 하차 : index[37]
        - 가장 많이 내리는 지하철역 순서로 정렬 후 5개의 지하철역 및 하차 인원수를 화면에 출력, 지하철 호선은 다르지만,
            동일한 이름의 역은 모두 합해서 계산함 하차 인원은 1,000단위로 콤마를 찍어서 구분할 것
        - bar 차트의 x축은 지하철역 이름을 표시하고, y축은 인원수를 표시
'''

import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

with open('subwaytime.csv', encoding='utf-8-sig') as f:
    data = csv.reader(f)
    next(data)
    next(data)
    station_dict= {}
    max_people = 0


    for row in data:
        row[4:]=map(int,row[4:])
        people = row[35] + row[37]
        if row[3] in station_dict:
            station_dict[row[3]] = station_dict[row[3]] + people
        else:
            station_dict[row[3]] = people

    xy = sorted(station_dict.items(), key=(lambda x : x[1]), reverse=True)[:5]
    print(xy)

x=[]
y=[]
for a,b in xy:
    x.append(a)
    y.append(b)
    print(f'{a}: {b:,}')


plt.bar(x,y)
plt.title('서울 지하철 퇴근 시간대 하차 인원 비교')
plt.show()



