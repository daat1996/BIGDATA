import pandas as pd



df = pd.read_excel('subway.xls', sheet_name='지하철 시간대별 이용현황', header=[0,1])
print(df.head())

# print(df.columns)   # 모든 컬럼내용 확인

# 멀티인덱스의 경우 튜플형식으로 접근
print(df[('호선명', 'Unnamed: 1_level_1')])
print(df[('지하철역', 'Unnamed: 3_level_1')])


commute_time_df = df.iloc[:,[1, 3, 10, 12, 14]]
print(commute_time_df.head())

print(commute_time_df.dtypes)

# 천단위 콤마(,) 제거 - .apply(lambda x : x.replace())
commute_time_df[('07:00:00~07:59:59', '승차')] = (commute_time_df[('07:00:00~07:59:59', '승차')].apply
                                                (lambda x : x.replace(',','')))
commute_time_df[('08:00:00~08:59:59', '승차')] = (commute_time_df[('08:00:00~08:59:59', '승차')].apply
                                                (lambda x : x.replace(',','')))
commute_time_df[('09:00:00~09:59:59', '승차')] = (commute_time_df[('09:00:00~09:59:59', '승차')].apply
                                                (lambda x : x.replace(',','')))

print(commute_time_df)


# 데이터타입 변경: object에서 int64로 변경 - .astype({'컬럼명':'int'})
commute_time_df = commute_time_df.astype({('07:00:00~07:59:59', '승차'):'int64'})
commute_time_df = commute_time_df.astype({('08:00:00~08:59:59', '승차'):'int64'})
commute_time_df = commute_time_df.astype({('09:00:00~09:59:59', '승차'):'int64'})
print(commute_time_df.dtypes)


row_sum_df = commute_time_df.sum(axis=1, numeric_only=True)



# 최댓값 및 최댓값 인덱스 찾기
# 최댓값 계산 : df.max(axis=0)
# 최댓값 인덱스 : df.idxmax()

max_number = row_sum_df.max(axis=0)
print(max_number)

max_index = row_sum_df.idxmax()
max_line, max_station = df.iloc[max_index, [1,3]]       # 최댓값의 [1]: 호선, [3]: 지하철역명
print('출근 시간대 최대 승차 인원역: {0} {1} {2:,}명'.format(max_line, max_station, max_number))