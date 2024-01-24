import csv
import matplotlib.pyplot as plt
import koreanize_matplotlib

f = open('../대구기온2-utf8.csv', encoding='utf-8-sig')
data = csv.reader(f)
next(data)
aug = []
jan = []

for row in data :
    month = row[0].split('-')[1]
    if row[-1] != '':
        if month =='08':
            aug.append(float(row[-1]))
        if month =='01':
            jan.append(float(row[-1]))


f.close()
plt.hist(aug, bins=100, color='tomato', label='Aug')
plt.hist(jan, bins=100, color='b', label='Jan')

plt.xlabel("Temperature")   # x축 레이블
plt.rc('axes', unicode_minus=False)     # 레이블에 '-'부호가 깨지는 현상 방지

plt.legend()
plt.show()