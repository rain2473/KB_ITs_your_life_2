
def start_game():
    import random
    com = random.randint(1,100)
    user=0
    correct=False
    for count in range(1,11):
        user = int(input("숫자를 맞춰 보세요 (1~100)"))
        print("%d회 시도"%count)
        if com == user:
            print("정답")
            correct = True
            break
        elif com< user:
            print("down")
        else:
            print("up")
        if count==10 and correct == False:  
            print("바보")
if __name__ == "__main__":           #모듈로 사용되는 경우 테스트코드 실행 안되게 함
    print(f'3+4={str(plus(3,4))}')
