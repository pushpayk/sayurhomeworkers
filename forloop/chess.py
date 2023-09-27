#problem 3#
#print chess board(alternate black and white squares)
#print('\u25A0') - will print white square. you can use "B" to print black squares

chess_board = int(input("please enter the squares :"))

for row in range(0,8):
    for column in range(0,8):
        if (row + column) % 2 == 0:
            print('\u25A1',end='')  #unicode character for white space
        else:
            print('\u25A0',end='')       #unicode characte for black space
    print()    # move to next row    
            
