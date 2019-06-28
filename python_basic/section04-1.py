##파이썬 데이터타입
##파이썬 데이터타입 종류
#Boolean, Numbers, String, Bytes, Lists, Tuples, Sets, Dictionaries

#Boolean : 1 / 0 (True / False)
#Numbers : integer, float...
#String : String
#Bytes : bytes
#List / Tuples / Sets / Dictionaries

v_str1 = "Woolbro Dev"
v_bool = True
v_str2 = "brother wool"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "Wool",
    "age" : 100
}
v_list = [3,5,7]
v_tuple = 3, 5, 7
v_set = {5,6,7,8,9}

print(type(v_list)) #type 안에 있는 변수의 형태를 출력
print(type(v_set))
print(type(v_tuple))

#
i1 = 39
i2 = 939
big_int1 = 99999999999999999999
big_int2 = 88888888888888888888
f1 = 1.23
f2 = 4.321
f3 = .5
f4 = 10.

print(f1 * f2)
print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2)
print(i1 + f2)

result = f1 * f2
print(result, type(result))


a = 5.
b = 4
c = 10

print(type(a), type(b))
result2 = a+b 
print(result2)

#형변환
# int, float, complex(복소수)

print(int(result2))
print(float(c))
print(complex(3))
print(int(True)) #print(int(False))
print(int('3'))
print(complex(False))


y = 100
y += 100 # y = y+100
## 연산자 뒤에 = 을 붙이면 위와 같이 연산 후 저장의 결과를 가져옴
print(y)

print(abs(-7))
n,m = divmod(100,8)
print(n,m)

import math
print(math.ceil(5.1))
print(math.floor(3.874))


#####
# python 숫자형 및 연산자
# + : 더하기
# - : 빼기
# * : 곱하기
# / : 나누기
# // : 나누기(몫)
# % : 나누기(나머지)
# ** : 지수(제곱)
######
