'''
    공공데이터 과제#1

    1. 과거 10년동안의 대구 날씨 데이터에서 1년중 일교차가 가장 큰 달은 각각 몇월인지 그래프로 표시
        - 기간 : 최근 10년 (2014년 ~ 2023년)
        - 각 달의 일교차(최고기온- 최저기온)을 비교하여 각 년도별 일교차가 가장 큰 달을 bar 그래프로 표시

'''
#1 모듈 설치
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib


# def draw_bar(title,x_data,max_dif_list,label_y):
#2-1 판다스로 csv자료 읽기(DataFrame)
weather_df=pd.read_csv('dague-utf8-df.csv', encoding='utf-8-sig')

#3-1 리스트설정(+ 빈 리스트 생성) 각 월별 최고 일교차 리스트 생성
year_list=[0]*10           # 1년간 각 월의 최대 일교차 저장

start_year = 2014



#3-2 df에서 datetime만 바꿔서 갖고옴
weather_df['날짜'] = pd.to_datetime(weather_df['날짜'], format='%Y-%m-%d')

#3-? 일교차 컬럼을 만든다
weather_df['일교차'] = weather_df['최고기온']-weather_df['최저기온']

#4-1 각 연별로 df 추출
for year in range(10):
    start_year_df = weather_df[weather_df['날짜'].dt.year==start_year + year]
    start_month = 1
    max_month=1
    month_diff_max = 0
    for month in range(12):
        start_month_df = start_year_df[start_year_df['날짜'].dt.month==start_month + month]
        month_mean=round(start_month_df['일교차'].mean(), 1)
        if month_diff_max < month_mean:
            month_diff_max = month_mean
            max_month = start_month + month
    year_list [year]=(start_year+year,max_month,month_diff_max)

x=[]
y=[]
for i in year_list:
    yea, m, c =i
    date = str(yea) + '.' + str(m)
    x.append(date)
    y.append(c)


print(year_list)
print(x)
plt.rcParams['axes.unicode_minus']=False
plt.figure(figsize=(10,4))
plt.bar(x,y)
plt.title('지난 10년간 대구의 일교차가 가장 큰 달')
plt.xlabel('Year/Month')
plt.ylabel('일교차')
plt.show()
#4-2 그 해의 최고 일교차와 해당 달을 리턴



