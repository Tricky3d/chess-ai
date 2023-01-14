import chess

board = chess.Board()

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
