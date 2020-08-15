#1
scores=[80,75,55]
total=0
for score in scores:
    total+=score

average=total/3
print(average)

#2
13%2

#3
pin="881120-1068234"
yymmdd=pin[:6]
num=pin[7:]
print(yymmdd)
num(pin)

#4
pin="881120-1068234"
print(pin[7])

#5
a="a:b:c:d"
b=a.replace(":","#")
print(b)

#6
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)

#7
a=['Life','is','too','short']
result=a.join()
print(result)

#8
a=(1,2,3)
a1=(4,)
a+a1

#9
##3-- 리스트는 dict의 key값으로 쓸 수 없음

#10
a={'A':90,'B':80,'C':70}
result=a.pop('B')
print(a)
print(result)

#11
a=[1,1,1,2,2,3,3,3,4,4,5]
aSet=set(a)
b=list(aSet)
print(b)

#12
[1,4,3]
##같은 리스트 객체를 가리키고 있기 때문