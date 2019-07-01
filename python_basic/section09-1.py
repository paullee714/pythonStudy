#Section 09-1
# 파일 읽기, 쓰기
# 읽기모드 : r , 쓰기모드 (기존파일 삭제) : w, 추가모드(파일 생성 또는 추가) : a
# .. : 상대경로 , . : 절대경로


# 파일 쓰기

# 예제 1
with open('resource/text1.txt','w') as f:
    f.write("woolbro dev file!!!")

# 예제 2
with open('resource/text1.txt','a') as f:
    f.write("\n Nice bro~ wool :)")


# 예제 3
from random import randint
with open('resource/text2.txt','w') as f:
    for cnt in range(6):
        f.write(str(randint(0,50)))
        f.write('\n')


with open('resource/log.txt','w') as f:
    print('log test 1',file=f)
    print('log test 2',file =f)