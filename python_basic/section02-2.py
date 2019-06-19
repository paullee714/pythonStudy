# Section02-2
# basic python coding

# import this #파이썬을 어떻게 써라~ 라고 나오는 부분
import sys

# 파이썬 기본 인코딩
# utf-8 기본 인코딩을 가지고있음.
# python 2.x 버전에서는 unicode 때문에 한글에 어려움이 있었음
print(sys.stdin.encoding) # 입력 인코딩의 기본 값
print(sys.stdout.encoding) # 출력 인코딩의 기본 값

# 출력문
print("My name is WoolBro!")

# 변수 선언
myName = 'Woolbro' #오른쪽에 있는 내용을 왼쪽으로..

# 조건문
if myName == 'Woolbro':
    print('Ok Same!')

# 반복문
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' %(i,j),i*j)

# 함수 선언

def sayHi():
    print("안녕하세요, 반갑습니다.") # 함수는 만들어놓고 사용을 해야 실행이 됨

sayHi()


# 클래스
class Cookie:
    # 속성, 메서드가 들어가는 곳
    pass

# 객체 생성(인스턴스)

cookie = Cookie()
print(id(cookie)) # id 라는 내장함수를 사용하여, cookie 객체의 정보를 출력
print(dir(cookie)) # dir라는 내장함수를 사용하여, cookie 객체의 정보를 출력