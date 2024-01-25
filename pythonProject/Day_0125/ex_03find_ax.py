'''
    최대 유임 승차 인원이 있는 역은?
    유임승차비율 = 유임승차인원 /전체승차인원 (유임+무임)

'''
import csv


f = open('subwayfee.csv', encoding='utf-8-sig')
data = csv.reader(f)
header = next(data)
max_rate= 0
for row in data:
    for i in range(4,8):
        row[i]=int(row[i])
    total_count = row[4] + row[6]
    if (row[6] != 0) and (total_count > 100000):
        # 무임승차(%) = (무스임 승차수 X100) / (유임승차 수 + 무임 승차 수)
        rate = row[4] / total_count
        if rate> max_rate:
            max_rate = rate
            max_row = row
            max_total_num = total_count

print()
print(f'호선명:{max_row[1]}, 역이름: {max_row[3]}, 전체 인원: {max_total_num:,}명,'
      f"유임승차인원: {max_row[4]:,}명, 유임승차비율: {round(max_rate * 100, 2)}%")

f.close()