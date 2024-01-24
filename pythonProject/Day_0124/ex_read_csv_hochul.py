import pandas as pd

weather_df = pd.read_csv('../대구기온2-utf8.csv', encoding='utf-8-sig')
print(weather_df.columns)
print(weather_df['날짜'].dtype)       # 날짜 컬럼은 object 타입

weather_df.columns=['날짜', '지점', '평균기온', '최저기온', '최고기온']
print(weather_df.columns)

weather_df['날짜'] = pd.to_datetime(weather_df['날짜'], format='%Y-%m-%d')
print(weather_df['날짜'].dtype)


print(weather_df.head())
print(weather_df.shape)
num_row = weather_df.shape[0]       # shape(row, col), shape[0]: row의 갯수
num_missing = num_row - weather_df.count()      # count(): 정상값의 개수
print(num_missing)

weather_df=weather_df.dropna(axis=0)
print(weather_df.count())
print(weather_df.head(5))

# 누락값을 제거한 최종 데이터를 csv파일로 저장
weather_df.to_csv('dague-utf8-df.csv',index=False, mode='w', encoding='utf-8-sig')

year_df = weather_df[weather_df['날짜'].dt.year == 2023]
month_df = year_df[year_df['날짜'].dt.month == 8]
print(month_df.head())

max_temp_mean = round(month_df['최고기온'].mean(),1)
min_temp_mean = round(month_df['최저기온'].mean(),1)

print(f'2023년 8월 최저기온 평균:{min_temp_mean}, 최고기온 평균:{max_temp_mean}')