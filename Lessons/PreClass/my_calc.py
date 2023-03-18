myname = '홍길동'

def plus(a,b):
    return a+b

def minus(a,b):
    return a-b

#모듈로 사용되는 경우 : __name__는 모듈명 저장
#독립실행된느 경우 : __main__로 저장

if __name__ == "__main__":           #모듈로 사용되는 경우 테스트코드 실행 안되게 함
    print(f'3+4={str(plus(3,4))}')
