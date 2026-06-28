"""
Project: Tic-Tac-Toe AI
Author: Sudduneeraja
Description: Human vs AI Tic-Tac-Toe using Minimax.
"""
import math

HUMAN="X"; AI="O"; EMPTY=" "

def create_board(): return [EMPTY]*9

def display_positions():
    print(" 1 | 2 | 3\n---+---+---\n 4 | 5 | 6\n---+---+---\n 7 | 8 | 9")

def display_board(b):
    print(f"\n {b[0]} | {b[1]} | {b[2]}")
    print("---+---+---")
    print(f" {b[3]} | {b[4]} | {b[5]}")
    print("---+---+---")
    print(f" {b[6]} | {b[7]} | {b[8]}\n")

def available_moves(b): return [i for i,v in enumerate(b) if v==EMPTY]

def check_winner(b,p):
    wins=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[a]==b[c]==b[d]==p for a,c,d in wins)

def is_draw(b): return EMPTY not in b

def make_move(b,pos,p): b[pos]=p

def player_move(b):
    while True:
        try:
            m=int(input("Enter move (1-9): "))
            if m<1 or m>9: print("Choose 1-9"); continue
            if b[m-1]!=EMPTY: print("Occupied."); continue
            return m-1
        except ValueError:
            print("Invalid input.")

def choose_first():
    while True:
        c=input("Play first? (Y/N): ").strip().lower()
        if c=="y": return HUMAN
        if c=="n": return AI

def minimax(b,depth,maxing):
    if check_winner(b,AI): return 10-depth
    if check_winner(b,HUMAN): return depth-10
    if is_draw(b): return 0
    if maxing:
        best=-math.inf
        for m in available_moves(b):
            b[m]=AI
            best=max(best,minimax(b,depth+1,False))
            b[m]=EMPTY
        return best
    best=math.inf
    for m in available_moves(b):
        b[m]=HUMAN
        best=min(best,minimax(b,depth+1,True))
        b[m]=EMPTY
    return best

def ai_move(b):
    best=-math.inf; move=None
    for m in available_moves(b):
        b[m]=AI
        score=minimax(b,0,False)
        b[m]=EMPTY
        if score>best:
            best=score; move=m
    make_move(b,move,AI)
    print("AI played.\n")

def main():
    human=ai=draw=0
    print("="*40)
    print("TIC-TAC-TOE AI (MINIMAX)")
    print("="*40)
    print("You will play as 'X'.")
    print("The AI will play as 'O'.")
    print("Enter numbers from 1-9 to place your mark")
    display_positions()
    while True:
        board=create_board()
        current=choose_first()
        while True:
            display_board(board)
            if current==HUMAN:
                make_move(board,player_move(board),HUMAN)
                if check_winner(board,HUMAN):
                    display_board(board); print("You win!"); human+=1; break
                current=AI
            else:
                ai_move(board)
                if check_winner(board,AI):
                    display_board(board); print("AI wins!"); ai+=1; break
                current=HUMAN
            if is_draw(board):
                display_board(board); print("Draw!"); draw+=1; break
        print(f"Score -> You:{human} AI:{ai} Draw:{draw}")
        if input("Play again? (Y/N): ").lower()!="y":
            print("Thanks for playing!")
            break

if __name__=="__main__":
    main()
