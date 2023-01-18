import chess

board = chess.Board()

for i in range(board.legal_moves.count()):
<<<<<<< HEAD
    el = list(board.legal_moves)
    
    

    move = str(el[i])

    movelist.append(str(el[i]))
    
    evalboard.push(chess.Move.from_uci(move))
    
    evalboard = board
    eval = 0
    alpha = float("-inf")
    beta = float("inf")
    evalist = list()
    movelist = list()
    for i in range(board.legal_moves.count()):
        el = list(board.legal_moves)
        move = str(el[i])
        movelist.append(str(el[i]))
        evalboard.push(chess.Move.from_uci(move))
        eval = material_balance(evalboard)
        if eval >= beta:
            evalboard.pop()
            break
        alpha = max(alpha, eval)
        for i in range(evalboard.legal_moves.count()):
            el = list(evalboard.legal_moves)
            evalboard.push(chess.Move.from_uci(str(el[i])))
            eval = material_balance(evalboard)
            if eval <= alpha:
                evalboard.pop()
                break
            beta = min(beta, eval)
            evalboard.pop()
        evalist.append(eval)
        evalboard.pop()
    bestmove = movelist[evalist.index(max(evalist))]
    board.push(chess.Move.from_uci(bestmove))
    print(board)
    
=======
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
>>>>>>> parent of 45d16e2 (khkh)
