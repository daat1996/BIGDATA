import pandas as pd



df = pd.read_excel('subway.xls', sheet_name='지하철 시간대별 이용현황', header=[0,1])
print(df.head())

# print(df.columns)   # 모든 컬럼내용 확인

# 멀티인덱스의 경우 튜플형식으로 접근
print(df[('호선명', 'Unnamed: 1_level_1')])
print(df[('지하철역', 'Unnamed: 3_level_1')])


