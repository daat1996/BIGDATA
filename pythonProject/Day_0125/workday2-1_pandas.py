import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

DF1 = pd.read_csv('subwaytime.csv',header=1,usecols=[1,3,11,13])
print(DF1)
DF1.columns = ['호선명', '지하철역', '7시하차','8시하차']
DF1['총하차'] = DF1['7시하차']+DF1['8시하차']
xticks=['']*7
y=[0]*7

for a in range(7):
    DF2=DF1[DF1['호선명'] == f'{a+1}호선'].sort_values(by='총하차',ascending=True)
    xticks=DF2['총하차'][0]


