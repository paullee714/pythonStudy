#Section 09
# 파일 읽기, 쓰기
# 읽기모드 : r , 쓰기모드 (기존파일 삭제) : w, 추가모드(파일 생성 또는 추가) : a
# .. : 상대경로 , . : 절대경로


# 파일 읽기
# 예제 1
file = open('resource/review.txt','r') #파일을 열 때에는, open이라는 함수.
content = file.read()
print(content)
file.close()

# 파일 읽기
# 예제 2
print("-----file open use <with>------------------------------------")
with open('resource/review.txt','r') as file_tmp:
    c = file_tmp.read()
    print(c)
    print(list(c)) ##c를 list화


# 파일 읽기
# 예제 3
print("---------file open use <with> line")
with open('resource/review.txt','r') as file_tmp:
    for c in file_tmp:
        print(c) ##라인단위로 출력

    for s in file_tmp:
        print(s.strip())


# 파일 읽기
# 예제 4
print("-----------file open")
with open('resource/review.txt','r') as file_tmp:
    content = file_tmp.read()
    print(">",content)
    content = file_tmp.read() ### 이 이후에는 파일의 커서가 맨 뒤로 가있기 때문에 
    print(">",content)        ### 읽지 못함(내용이 없음)
    

# 파일 읽기
# 예제 5
print("-----------file open")
with open('resource/review.txt','r') as file_tmp:
    line = file_tmp.readline()
    #print(line) #한줄만 읽어서 가져오기 때문에 반복문이 필요
    while line:
        print(line, end = ' ')
        line = file_tmp.readline()
    