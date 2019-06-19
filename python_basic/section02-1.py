# Section02-1 
# basic python coding
# print

print('Hello Python!') #task runner ctrl+shift+b
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')


# Separator Option Usage
print('T','E','S','T') ## T E S T
print('T','E','S','T' , sep='')
print('2019','02','19',sep='-')
print('nicemkan' ,'google.com', sep='@')


#end option usage
print('Welcom To', end='')
print('the black parade', end='')
print(' paino notes')

#format 사용
print('{} and {}'.format('You','Me'))
print("{0} and {1} and {0}".format('You','Me'))
print("{a} are {b}".format(a='You' , b="Me"))

print("%s's favorite number is %d"% ('WoolBro',7)) # %s : 문자 , %d : 정수, %f : 실수
print("Test1 : %5d, Price: %4.2f"%(700,6543.211))
print("Test1 : {0: 5d}, Price:{1: 4.2f}".format(700,6543.211))
print("Test1 : {a:5d}, Price:{b: 4.2f}".format(a=700,b=6543.211))



print(""" Lorem Ipsum is simply dummy te
xt of the printing and typesetting industry. Lorem Ipsum h
as been the industry's standard dummy text ever since the 1500s, when an unknow
n printer took a galley of type and scrambled it to make a type specimen book. It has 
survived not only five centuries, but also the leap into electronic typesetting, remaining
 essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets c
 ontaining Lorem Ipsum passages, and more recently with desktop
 publishing software like Aldus PageMaker including versions of Lorem Ipsum.""")