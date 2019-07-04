#Section10
#파이썬 예외처리의 이해

#예외를 강제로 발생 시키고, 처리를 해보도록하자
# 예외의 종류를 외울 수 는 없지만, 알아 둘 것은 알아두자.


# 예외 종류
# 문법적으로 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 예외 처리도 중요.
# linter : 코드 스타일, 문법 체크


# # SytanxError  - 잘못된 문법
# print('Test)
# if True
#     print('Hi')
# x => y


# # NameError
# a = 10
# b = 15
# print(c)


#ZeroDivisionError : 0으로 나누기 에러
# print(30/0)


# #IndexError : 인덱스 범위 오류
# x = [10,20,30]
# print(x[0]) #정상
# print(x[4]) # IndexError

# # KeyError
# dic = {'name' : 'woolbro' , 'Age' : 100 , 'City' : 'Bundang' }
# print(dic['hobby']) # 없는 키를 사용...
# print(dic.get('hobby')) # get 메소드로,  dictionary 내부에 키의 여부를 검사

# #AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용
# import time
# print(time.time())
# print(time.month()) ## 에러 발생...!!!

# # ValueError : 참조 값이 없을 때 발생
# x = [1, 5, 10]
# x.remove(100)

# FileNotFoundError : 파일이 없을 때
# f = open('wooldev.txt','r') # 예외 발생 .... wooldev.txt가 없기 때문에


# #TypeError : Type이 맞지 않을 경우
# x = [1,2,3,4]
# y = {1,2,3,4,5}
# z = 'test wool String'

# print(x+y) # x와 y의 자료형이 다르다... tuple과 list의 연산...
# print(x+z) # 문자열과 리스트는 결합 할 수 없다.....
# print(x+list(y)) # 형변환을 사용해 위의 오류를 해결....





#예외처리
# try-except-else-finally

#예제 1
name = ['wool','lee','dev']
try:
    z = 'wool'
    x = name.index(z)
    print(" {} : name리스트에서 찾았다! ".format(z,x+1))
except ValueError:
    print('Not Fount it! - Occured ValueError!!!')
else:
    print(' OK!!! else!!')
finally:
    print('work is done....')


#예외처리
# try-except-else-finally

#예제 2
# 어떤 에러가 발생할지 모를 경우 except는 그냥 사용...
name = ['wool','lee','dev']
try:
    z = 'bro'
    x = name.index(z)
    print(" {} : name리스트에서 찾았다! ".format(z,x+1))
except :
    print('Not Fount it! - Occured Error!!!!')
else:
    print(' OK!!! else!!')
finally:
    print('work is done....')


#예제 3
# 어떤 에러가 발생할지 모를 경우 except는 그냥 사용...
name = ['wool','lee','dev']
try:
    z = 'bro'
    x = name.index(z)
    print(" {} : name리스트에서 찾았다! ".format(z,x+1))
except :
    print('Not Fount it! - Occured Error!!!!')
else:
    print(' OK!!! else!!')
finally:
    print('work is done....')

# 예제 4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'kim'
    if a == 'wool':
        print('ok 허가!')
    else:
        raise ValueError
except ValueError:
    print("wool이 아닙니다")
else:
    print('Ok')
finally:
    print('Program is done.....')
