board_size=9
def creat_board(size=board_size):
    return [[0 for _ in range(size)] for _ in range(size)]

def print_board(board):
    symbol={
        0:'.',
        1:'B',
        2:'W'
    }
    print('  '+' '.join(str(m+1) for m in range(board_size))) 

    for i,row in enumerate(board):
        row_symbols=[symbol[cell] for cell in row]
        print(str(i+1) + ' ' + ' '.join(row_symbols))
        
def place_stone(board,row,col,player):
    board[row][col]=player

def check_valid(row,col):
    return 0<=row < board_size and 0 <=col < board_size

def check_win(board,row,col,player):
    count=1
    directions=[
        (0,1), # horizontal 
        (1,0), # vertical
        (1,-1),# diagonal
        (1,1) # diagonal
    ]
    for dr,dc in directions:
        r=row+dr
        c=col+dc
        
        while check_valid(r,c) and board[r][c] ==player:
            count+=1
            r+=dr
            c+=dc
            
        r=row-dr
        c=col-dc
        
        while check_valid(r,c) and board[r][c]==player:
            count+=1
            r-=dr
            c-=dc
        
        if count>=5:
            return True
    return False

def is_valid_move(board,row,col):
    if not check_valid(row,col):
        return False
    if board[row][col]!=0:
        return False
    return True

def main():
    
    board=creat_board()

    current_player=1

    while True:
        print_board(board)
    
        if current_player==1:
            print('Black to move')
        else:
            print('white to move')
    
        move = input('Enter your choice(row and col)')
        user_row,user_col=map(int,move.split())
        row=user_row-1
        col=user_col-1
        if is_valid_move(board,row,col):       
            place_stone(board,row,col,current_player)
    
            if check_win(board,row,col,current_player):
                print_board(board)
            
                if current_player==1:
                    print("black wins!")
                else:
                    print("white wins!")
            
                break
            if current_player==1:
                current_player=2
            else:
                current_player=1
        else:
            print("invalid move")

if __name__=='__main__':
    main()
    