previous=0
current=1
i=0

while i<20:
    print(current)
    temp=previous
    previous=current
    current=temp+current
    i=i+1