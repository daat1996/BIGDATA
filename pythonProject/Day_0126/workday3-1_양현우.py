'''
    공공데이터 과제 #3
    1. 대구광역시 전체 및 8개 구,군별(군위 제외) 남녀비율을 각각의 파이차트로 구현하세요
        - subplots를 이용하여 3x3 형태의 총 9개의 subplot을 파이차트로 구현
        - gender.csv 파일 사용
'''




import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

f = open('gender.csv',encoding='utf-8-sig')
data = csv.reader(f)
city_list = ['대구광역시','대구광역시 중구', '대구광역시 동구', '대구광역시 서구',
             '대구광역시 남구', '대구광역시 북구', '대구광역시 수성구', '대구광역시 달서구',
             '대구광역시 달성군']

plt.figure(figsize=(10,10))

for a in range(9):
    population_list=[]

    f.seek(0)
    for row in data:
        if city_list[a] in row[0]:
            male_count = int(row[104].replace(',',''))
            population_list.append(male_count)
            female_count = int(row[207].replace(',',''))
            population_list.append(female_count)
            break
    # print(population_list)

    plt.subplot(3, 3, a+1)
    color = ['cornflowerblue','tomato']
    plt.title(f'{city_list[a]}')

    plt.pie(population_list,labels=['남','여'],autopct='%.1f%%', startangle=90)

plt.suptitle('대구광역시 구별 남녀 인구 비율\n', size=15)
plt.tight_layout()
plt.show()