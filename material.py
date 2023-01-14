import chess
import chess.polyglot
import chess.svg
import Pool




board = chess.Board()
highesteval = -10000
bestmove = "e"
def material_balance(board):
    white = board.occupied_co[chess.WHITE]
    black = board.occupied_co[chess.BLACK]
    return (
        chess.popcount(white & board.pawns) - chess.popcount(black & board.pawns) +
        3 * (chess.popcount(white & board.knights) - chess.popcount(black & board.knights)) +
        3 * (chess.popcount(white & board.bishops) - chess.popcount(black & board.bishops)) +
        5 * (chess.popcount(white & board.rooks) - chess.popcount(black & board.rooks)) +
        9 * (chess.popcount(white & board.queens) - chess.popcount(black & board.queens))
    )

boardsvg = chess.svg.board(board, size=300) 

outputfile = open('e.svg', "w")
outputfile.write(boardsvg)
outputfile.close()


e  = board.legal_moves.count() - 1
print(board)

while True:
  
    el = list(board.legal_moves)
  
    e  = board.legal_moves.count() - 1
    highesteval = -1000
    
        
    Pool.get_move(board)   
        
    if(Pool.get_move(board) == True):   
        
        open = str(Pool.move)
        print() 
        board.push(chess.Move.from_uci(open))
        print(board)

        board.push(chess.Move.from_uci(input("user move: ")))
        
    else:
        for i in range(board.legal_moves.count()):
            el = list(board.legal_moves)
            evalboard = board
            eval = 0
    
            move = str(el[i-1])
            
            evalboard.push(chess.Move.from_uci(move))
            for i in range(evalboard.legal_moves.count()):
                el = list(evalboard.legal_moves)
                evalboard.push(chess.Move.from_uci(str(el[i-1])))
                for i in range(evalboard.legal_moves.count()):
                    el = list(evalboard.legal_moves)
                    evalboard.push(chess.Move.from_uci(str(el[i-1])))
                    for i in range(evalboard.legal_moves.count()):
                        el = list(evalboard.legal_moves)
                        evalboard.push(chess.Move.from_uci(str(el[i-1])))
                        for i in range(evalboard.legal_moves.count()):
                            el = list(evalboard.legal_moves)
                            evalboard.push(chess.Move.from_uci(str(el[i-1])))
                            evalboard.pop()
                        evalboard.pop()
                    evalboard.pop()
                evalboard.pop()
            evalboard.pop()
        board.push(chess.Move.from_uci(bestmove))
        print(board)
        boardsvg = chess.svg.board(board, size=300) 

       
        board.push(chess.Move.from_uci(input("user move: ")))
        print(board)
        


   
    if(str(board.outcome()) != "None"):
        print(board.outcome())
        print(board)
        boardsvg = chess.svg.board(board, size=300) 

        outputfile = open('e.svg', "w")
        outputfile.write(boardsvg)
        outputfile.close()
        exit()



