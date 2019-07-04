# Section 11
# 파이썬 외부 파일 처리
# Excel, CSV 파일 처리


# CSV : MIME 형식(text/csv 파일)

import csv # CSV 파일을 핸들링 하기 위한 모듈


# 예제 1번
with open('./resource/sample1.csv','r') as f:
    reader  = csv.reader(f)

    #확인하기
    print(reader)
    print(type(reader))
    print(dir(reader))


    for txt in reader:
        print(txt)


# 예제 2번
with open('./resource/sample2.csv','r') as f:
    reader  = csv.reader(f,delimiter = '|')

    #확인하기
    print()
    print()
    print()


    for txt in reader:
        print(txt)



# 예제 3번( Dictionary)
with open('./resource/sample1.csv','r') as f:
    reader = csv.DictReader(f)
    # for c in reader:
    #     print(c)
    for c in reader:
        for k, v in c.items():
            print(k, v)
        print("===================")



# 예제 4번
data = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]] # 이차원 리스트

with open('./resource/sample_test.csv','w', newline='') as f:
    makewrite = csv.writer(f)

    for value in data:
        makewrite.writerow(value)


#예제 5
# for 문을 사용하지 않고 한번에 쓰기

with open('./resource/sample4.csv','w',newline='') as f:
    wt = csv.writer(f)
    wt.writerows(data)


print()
print()
print()

# XSL, XLSX
# PANDAS
# install
# pip install xlrd
# pip install openpyxl
# pip install pandas


import pandas as pd
#sheetname = '시트명 or 숫자' , header = 숫자 skiprow=숫자
xlsx = pd.read_excel('./resource/sample.xlsx')
#상위 데이터 확인
print(xlsx.head())
print()
print(xlsx.tail())
print()
print(xlsx.shape) #행, 열

print()


# 엑셀, CSV 다시 쓰기
xlsx.to_excel('./resource/pandas_result.xlsx',index=False) # index : 첫 열에 숫자 붙여주기
xlsx.to_csv('./resource/pandas_csv.csv',index=False)
