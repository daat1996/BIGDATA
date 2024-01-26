import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

f = open('gender.csv', encoding='utf=8-sig')
data = csv.reader(f)

city = input('찾고 싶은 지역의 이름을 입력하세요: ')
male_count = 0
female_count = 0

for row in data:
    if city in row[0]:
        male_count = int(row[104].replace(',',''))
        female_count = int(row[207].replace(',',''))
        break       # 도시별 하위목록이 많기에 처음 나오는 데이터가 전체의 총합이다.

print(f'{city} 남자인구수: {male_count:,}명, 여자인구수: {female_count:,}명')

population=[male_count,female_count]    # pie 차트에 넣을 데이터, (남,녀 인구수)
color = ['cornflowerblue','tomato']
plt.pie(population,labels=['남','여'], autopct='%.1f%%', colors=color, startangle=90)
plt.title(city + '남녀 성별 비율')
plt.show()