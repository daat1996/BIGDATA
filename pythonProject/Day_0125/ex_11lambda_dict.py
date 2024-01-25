'''
    lambda를 이용한 정렬

'''
import operator

names = {'Mary':10999, 'Sams':2111,	'Aimy':9778, 'Tom':20245, 'Michale':27115, 'Bob':5887, 'Kelly':7855}

# Key 를 기준으로 정렬
print('[lambda] dict정렬: key 기준, 오름차순')
res = sorted(names.items(), key=(lambda x: x[0]))
print(res)
print()

# Value 를 기준으로 정렬, 내림차순
print('[lambda] dict정렬: key 기준, 내림차순')
res = sorted(names.items(), key=(lambda x: x[1]), reverse=True)
print(res)

'''
    operator 모듈을 이용한 정렬
'''
# Key 를 기준으로 정렬
sorted_x = sorted(names.items(), key=operator.itemgetter(0))
print('[operator] dict정렬: key 기준, 오름차순')
print(sorted_x)
print()

# Value 를 기준으로 정렬, 내림차순
sorted_x = sorted(names.items(), key=operator.itemgetter(1), reverse=True)
print('[operator] dict정렬: value 기준, 내림차순')
print(sorted_x)