import chess
import chess.polyglot
import chess.svg
import Pool

opens = True

on = True

board = chess.Board()
highesteval = -10000
bestmove = "e"
def calc_eval(board):
    white = board.occupied_co[chess.WHITE]
    black = board.occupied_co[chess.BLACK]
    if board.is_checkmate() == True:
        return 99999
    else: 

        return (
            chess.popcount(white & board.pawns) - chess.popcount(black & board.pawns) +
            3 * (chess.popcount(white & board.knights) - chess.popcount(black & board.knights)) +
            3 * (chess.popcount(white & board.bishops) - chess.popcount(black & board.bishops)) +
            5 * (chess.popcount(white & board.rooks) - chess.popcount(black & board.rooks)) +
            9 * (chess.popcount(white & board.queens) - chess.popcount(black & board.queens))
        )


boardsvg = chess.svg.board(board, size=300)

with open("e.svg", "w", encoding="utf-8") as outputfile:
    outputfile.write(boardsvg)

e  = board.legal_moves.count() - 1
print(board)

while opens == True:
  
    el = list(board.legal_moves)
  
    e  = board.legal_moves.count() - 1
    highesteval = 1000
    high = -1000
        
    Pool.get_move(board)   
        
    if(Pool.get_move(board) == True):   
        
        opend = str(Pool.move)
        print() 
        board.push(chess.Move.from_uci(opend))
        print(board, "\n")
        

    else:
        opens = False   

pose = 0
def minimax(board, depth, maximizing_player, alpha, beta): #table is board
    global pose
    children = list(board.legal_moves) #find all possible moves from certain position

    if depth == 0 or board.is_game_over(): #don't go deeper if game over/depth ended
        return calc_eval(board), None #calc-eval finds piece-values on board and adds them up. e.g. two pawns would be 2 points

    if maximizing_player == True:
        best_value = -float("Inf")
    else:
        best_value = float("Inf")

    for child in children:
        pose += 1
        board.push(child) #copy board and change it by moving the child move
        new_val = minimax(board, depth - 1, not maximizing_player, alpha, beta)[0] #recursively find value
        board.pop()
        if maximizing_player == True and new_val > best_value:
            best_value = new_val
            best_move = child
            alpha = max(alpha, best_value)
        if maximizing_player == False and new_val < best_value:
            best_value = new_val
            best_move = child
            beta = min(beta, best_value)
        if alpha > beta:
            break

    return best_value, best_move

while True:
    g = minimax(board,3,True, -100000, 100000)[1]
    board.push_uci(str(g))
    print(board, "\n")
    boardsvg = chess.svg.board(board, size=300)
    
    if board.is_checkmate() == True:
        print("Unlucky for black")
        break
    g = minimax(board,3,False, -100000, 100000)[1]
    board.push_uci(str(g))
    print(board, "\n")
    if board.is_checkmate() == True:
        print("Unlucky for white")
        break

