#1
def is_odd(a):
    if a%2==0:
        return "even"
    else:
        return "odd"
        
#2
def average(*args):
    result=0
    for i in args:
            result+=i
    return result/len(args)

#3
input1=input("첫 번째 숫자를 입력하세요: ")
input2=input("두 번째 숫자를 입력하세요: ")

total=int(input1)+int(input2)
print("두 수의 합은 %s입니다" %total)

#4
##3번: you need python

#5
f1=open("text.txt",'w')
f1.write("Life is too short")
f1.close()

f2=open("text.txt",'r')
print(f2.read())

#6
f=open("test.txt",'a')
data=input()
f.write(data)
f.close()

#7
f=open('test.txt', 'w')
data="Life is too short you need java"
f.write(data)
f.replace("java","python")
f.close()
