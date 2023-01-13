import chess
import chess.polyglot

board = chess.Board()
board.push_uci("e2e4")
board.push_uci("e7e5")
board.push_uci("g1f3")
board.push_uci("b8c6")
board.push_uci("f1c4")
board.push_uci("e8e7")
w = 0
move = "e"
domove = True
count = 0
lastmove = "odfspfspfkspkfp"



def get_move(board):
    with chess.polyglot.open_reader("/Users/max/Downloads/poly17/books/Perfect2017.bin") as reader:
        for entry in reader.find_all(board):
            
            global move, w, domove, count, lastmove
            w = 0
            w = entry.weight
            move = entry.move
            print(move, lastmove)
            if(str(move) != str(lastmove)):
                return True
            lastmove = move
            break
   
