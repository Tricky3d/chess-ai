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
    
        
    
        
    if(Pool.get_move(board) == True):   
        Pool.get_move(board)   
        open = str(Pool.move)
        print() 
        board.push(chess.Move.from_uci(open))
        print(board)

        board.push_san(input("user move: "))
        
    else:
        evalboard = board
        eval = 0
        evalist = list()
        evalist1 = list()
        evalist2 = list()
        evalist3 = list()
        movelist = list()
        for i in range(board.legal_moves.count()):
            el = list(board.legal_moves)
            
            
    
            move = str(el[i])

            movelist.append(str(el[i]))
            
            evalboard.push(chess.Move.from_uci(move))
            
            for i in range(evalboard.legal_moves.count()):
                el = list(evalboard.legal_moves)
                evalboard.push(chess.Move.from_uci(str(el[i])))
                for i in range(evalboard.legal_moves.count()):
                    el = list(evalboard.legal_moves)
                    evalboard.push(chess.Move.from_uci(str(el[i])))
                    for i in range(evalboard.legal_moves.count()):
                        el = list(evalboard.legal_moves)
                        evalboard.push(chess.Move.from_uci(str(el[i])))
                        eval = material_balance(evalboard)
                        
                        evalist.append(eval)
                        evalboard.pop()
                    evalist1.append(evalist[evalist.index(min(evalist))])
                    evalboard.pop()
                evalist2.append(evalist1[evalist1.index(max(evalist1))])
                evalboard.pop()
            evalist3.append(evalist2[evalist2.index(min(evalist2))])
            evalboard.pop()
        bestmove = movelist[evalist3[evalist3.index(max(evalist3))]]
        board.push(chess.Move.from_uci(bestmove))
        print(board)
        boardsvg = chess.svg.board(board, size=300) 

       
        board.push_san(input("user move: "))
        print(board)
        


   
    if(str(board.outcome()) != "None"):
        print(board.outcome())
        print(board)
        boardsvg = chess.svg.board(board, size=300) 

        outputfile = open('e.svg', "w")
        outputfile.write(boardsvg)
        outputfile.close()
        exit()



