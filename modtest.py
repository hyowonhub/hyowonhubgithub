from random import randint
answer=randint(1,20)
trial=0

while trial<=4:
    chance=4-trial
    inPut=int(input(f"기회가 {chance}번 남았습니다. 1-20 사이의 숫자를 맞춰보세요: "))
    print(inPut)
    if inPut==answer:
        trial=trial+1
        print(f"축하합니다. {trial}번만에 숫자를 맞추셨습니다.")
        break
    elif inPut>answer:
        print("Down")
        trial=trial+1
        continue
    else:
        print("Up")
        trial=trial+1
        continue
        
    print(f"아쉽습니다. 정답은 {answer}였습니다.")