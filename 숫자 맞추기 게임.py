number=int(input("한 자리 숫자를 맞쳐보세요: "))
while number !=8:
        if number<8:
            print("정답보다 작은 수 입니다. 다시 시도해 보세요.")
            break
        elif 10>number>8:
            print("정답보다 큰 수 입니다. 다시 시도해 보세요")
            break
        else:
            print("<한 자리> 숫자를 맞쳐보세요. 다시 시도해 보세요")
if number==8:
    print("정답입니다!")
