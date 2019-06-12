# hello.py

a = 1
b = 1
a = 2

if a > 1 :
    print('big')
    print('big')

    for i in range(1, 10):
        print('-->', i) # 가변파라미터

print('end')

# 들여쓰기로 block을 구분하여 if 문의 끝을 알 수 있음.

def add(m, n):
    s=m
    s+=n
    return s;

def max(m, n):
    if m > n :
        return m
    else:
        return n