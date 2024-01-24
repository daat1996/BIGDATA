'''
    공공데이터 과제#2

    1. 대구 기온데이터에서 시작 연도, 마지막 연도를 입력하고 특정월의 최고기온 및 최저 기온의 평균값을 구하고 그래프
        - 화면에서 측정할 달을 입력 받아서 진행
        - 각 달의 일교차(최고기온- 최저기온)을 비교하여 각 년도별 일교차가 가장 큰 달을 bar 그래프로 표시

'''
#1 모듈 설치
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib


def drag_two_plot(title,x_data,max_temp,max_label,min_temp,min_label):
    plt.rc('axes',unicode_minus=False)
    plt.figure(figsize=(19,4))
    plt.title(title)
    plt.plot(x_data,max_temp, marker='s', markersize=6, color='r', label=max_label)
    plt.plot(x_data,min_temp, marker='s', markersize=6, color='b', label=min_label)
    plt.xticks(x_data)
    plt.legend()
    plt.show()






def main():
    weather_df=pd.read_csv('dague-utf8-df.csv',encoding='utf-8-sig')
    weather_df['날짜'] = pd.to_datetime(weather_df['날짜'], format='%Y-%m-%d')      # 연-월-일

    start_year=int(input(f'시작 연도를 입력하세요: '))
    end_year=int(input(f'마지막 연도를 입력하세요: '))
    s_month=int(input(f'기온 변화를 측정할 달을 입력하세요: '))
    print(f'{start_year}년부터 {end_year}년까지 {s_month}월의 기온 변화')

    start_year_df_max=[]
    start_year_df_min=[]
    for year in range(end_year-start_year+1):
        start_year_df=weather_df[(weather_df['날짜'].dt.year==start_year+year) &
                                 (weather_df['날짜'].dt.month == s_month) ]
        start_year_df_max.append(round(start_year_df['최고기온'].mean(),1))
        start_year_df_min.append(round(start_year_df['최저기온'].mean(),1))
    print(f'{s_month}월 최저기온 평균:\n{str(start_year_df_min)[1:-1]}')
    print(f'{s_month}월 최고기온 평균:\n{str(start_year_df_max)[1:-1]}')
    x_data=[a for a in range(start_year,end_year+1)]
    title=f'{start_year}년부터 {end_year}년까지 {s_month}월의 기온 변화'

    drag_two_plot(title,x_data,start_year_df_max,'최고기온', start_year_df_min,'최저기온')


main()