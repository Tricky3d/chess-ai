import chess

board = chess.Board()
evalboard = board
eval = 0
evalist = list()
evalist1 = list()
evalist2 = list()
evalist3 = list()
movelist = list()

board.push_san("e4")
board.push_san("e5")
board.push_san("Nf3")
board.push_san("Ke7")




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
for i in range(board.legal_moves.count()):
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
    
