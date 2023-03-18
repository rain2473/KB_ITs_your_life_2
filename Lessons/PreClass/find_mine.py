import random
play = True
count = 0

def fields_create() as fields():
    fields = list()
    for i in range(10):
        fields.append([0]*10)
    return fields

def mine_create():
    fields()
    nums = list(range(100))
    for i in random.sample(nums,10):
        col = i//10
        row = i%10
        fields[col][row] = 9
        if 0<col<9 and 0<row<9:
            fields[col+1][row+1] += 1 #남동
            fields[col-1][row+1] += 1 #북동
            fields[col+1][row] += 1   #남
            fields[col-1][row] += 1   #북
            fields[col+1][row-1] += 1 #남서
            fields[col-1][row-1] += 1 #북서
            fields[col][row+1] += 1   #동
            fields[col][row-1] += 1   #서
        elif col == 0 and 0<row<9:
            fields[col+1][row+1] += 1 #남동
            fields[col+1][row] += 1   #남
            fields[col+1][row-1] += 1 #남서
            fields[col][row+1] += 1   #동
            fields[col][row-1] += 1   #서
        elif col==9 and 0<row<9:
            fields[col-1][row+1] += 1 #북동
            fields[col-1][row] += 1   #북
            fields[col-1][row-1] += 1 #북서
            fields[col][row+1] += 1   #동
            fields[col][row-1] += 1   #서
        elif 0<col<9 and row == 0:
            fields[col+1][row+1] += 1 #남동
            fields[col-1][row+1] += 1 #북동
            fields[col+1][row] += 1   #남
            fields[col-1][row] += 1   #북
            fields[col][row+1] += 1   #동
        elif 0<col<9 and row==9:
            fields[col+1][row] += 1   #남
            fields[col-1][row] += 1   #북
            fields[col+1][row-1] += 1 #남서
            fields[col-1][row-1] += 1 #북서
            fields[col][row-1] += 1   #서
        elif col == 0 and row == 0:
            fields[col+1][row+1] += 1 #남동
            fields[col+1][row] += 1   #남
            fields[col][row+1] += 1   #동
        elif col==9 and row==0:
            fields[col-1][row+1] += 1 #북동
            fields[col-1][row] += 1   #북
            fields[col][row+1] += 1   #동
        elif col==0 and row==9:
            fields[col+1][row-1] += 1 #남동
            fields[col+1][row] += 1   #남
            fields[col][row-1] += 1   #동
        elif col==9 and row==9:
            fields[col-1][row] += 1   #북
            fields[col-1][row-1] += 1 #북서
            fields[col][row-1] += 1   #서
            
def player_create() as player():
    player = list()
    for i in range(10):
        player.append(['']*10)
    return player

def game_start():
    mine_create()
    player()

    while play == True:
        display(player)
        input_player=int(input("좌표를 입력하세요 0~99: "))
        if fields[input_player//10][input_player%10] > 8:
                print('축하합니다 찾았습니다!!')
                player[input_player//10][input_player%10]=fields[input_player//10][input_player%10]
                count+=1
                if count == 10:
                    print('축하합니다 모두 찾았습니다!!')
                    display(fields)
                    break

                else:
                    print(f'{count}개 찾았습니다 {10-count}개 남았습니다')

        else:
                player[input_player//10][input_player%10]=fields[input_player//10][input_player%10]
                print("\r")