'''
    마방진 만들기
'''

# num = 5

def print_mine(list):           # 확인용
    for a in list:
        for b in a:
            print(f'{b:2d}', end=' ')
        print()



mix_list = []
key = 1

while key == 1:
    num = int(input('1보다 큰 홀수를 입력하세요: '))
    if num ==4:
        key = 4
    else:
        if num % 2 ==0:
            print('짝수를 입력하였습니다. 다시 입력하세요')
        else:
            key = 2
    for i in range(num):
        mix_list.append([0]*num)


def make_x(x):
    global num
    if 0<x+1<num:
        x += 1
    else:
        x = 0
    return x

def make_y(y):
    global num
    if 0<=y-1<num:
        y -= 1
    else:
        y = num-1
    return y


def dmake_y(y):
    global num
    if 0<y+1<num:
        y += 1
    else:
        y = 0
    return y




# print_mine(mix_list)
# 기본조건 - 1의 값은 첫행 중간열, 다음 값은 행,열 + 1

# 2가지 조건
#       - x,y는 0이상 num 미만을 가져야함 => 크면 0으로, 작으면 num으로 리턴
#       - 리스트가 0이 아닐경우 행값(y)이 1 커진다.

while key ==2:

    y=0
    x=num//2
    for a in range(1,num**2+1):
        mix_list[y][x] = a
        if mix_list[make_y(y)][make_x(x)]==0:
            x = make_x(x)
            y = make_y(y)
        else:
            y= dmake_y(y)



    print_mine(mix_list)
    key=3
# print_mine(mix_list)

if key ==4:
    list4 = [[16,2,3,13],[5,11,10,8],[9,7,6,12],[4,14,15,1]]
    print_mine(list4)
