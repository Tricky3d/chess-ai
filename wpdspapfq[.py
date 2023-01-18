        evalboard = board
        eval = 0
        bestvalue = float("inf")
        
        evalist = list()
        evalist1 = list()
        evalist2 = list()
        evalist3 = list()
        movelist = list()
        for i in range(board.legal_moves.count()):
            el = list(board.legal_moves)
            beta = float("-inf")
            bestvalue = float("inf")
    
            move = str(el[i])

            movelist.append(str(el[i]))
            
            evalboard.push(chess.Move.from_uci(move))
            
            for i in range(evalboard.legal_moves.count()):
                el = list(evalboard.legal_moves)
                evalboard.push(chess.Move.from_uci(str(el[i])))
                for move in range(evalboard.legal_moves.count()):
                    el = list(evalboard.legal_moves)
                    evalboard.push(chess.Move.from_uci(str(el[move])))
                    for i in range(evalboard.legal_moves.count()):
                        el = list(evalboard.legal_moves)
                        evalboard.push(chess.Move.from_uci(str(el[i])))
                        eval = material_balance(evalboard)
                        evalist.append(eval)
                        bestvalue = min(bestvalue, eval)
                        evalboard.pop()
                        
                    beta = bestvalue
                    evalist1.append(bestvalue)
                    evalist = list()
                    evalboard.pop()
                evalist2.append(evalist1[evalist1.index(max(evalist1))])
                evalist1 = list()
                evalboard.pop()
            evalist3.append(evalist2[evalist2.index(min(evalist2))])
            evalist2 = list()
            evalboard.pop()
        bestmove = movelist[evalist3.index(max(evalist3))]