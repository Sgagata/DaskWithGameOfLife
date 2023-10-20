import sys
import numpy as np

def main():
    try:
        input_name = sys.argv[1]
    except IndexError:
        sys.exit("No output filename")
    try:
        output_name= sys.argv[2]
    except IndexError:
        sys.exit("No output filename")
    try:
        n = int (sys.argv[3])
    except:
        sys.exit(f"Entered value is not a nuber {sys.argv[3]}")
    board = read_input_file(input_name)
    final_board = play_game(board, n)
    write_output_file(output_name, final_board)
          
def read_input_file(input_file):
    # initialize board
    with open(input_file) as f:
        w, h = [int(x) for x in next(f).split()]
        # use the smallest data type
        board = np.zeros((w, h),dtype=np.uint8)
        for line_count, line in enumerate(f, start=0):
            single_numbers = line.split()
            x, y = map(int, single_numbers[:2])
            board[x][y] = 1
    return board
                

def write_output_file(output, board):
    w = board.shape[0]
    h = board.shape[1]
    live_cells = []
    for r in range(w):
        for c in range(h):
            if board[r][c] == 1:
                live_cells.append([r, c])
    f = open(output, "w")
    f.write(str(w)+ " "+ str(h)+"\n")
    for cell in live_cells:
        f.write(str(cell[0])+ " "+ str(cell[1])+ "\n")
    f.close()
    
def initialize_board(w, h, live_cells):
    board = np.zeros((w, h))
    for cell in live_cells:
        board[cell[0]][cell[1]]=1
    return board

def neighbors_number(board, row, col):
    # add plus two to create a proper iteration
    neighbors = board[max(0, row-1):min(board.shape[0], row+2), max(0, col-1):min(board.shape[1], col+2)]
    return np.sum(neighbors) - board[row, col]

def play_game(board, iterations):
    for i in range(iterations):
        new_board = board.copy()
        for r in range(board.shape[0]):
            for c in range(board.shape[1]):
                #for dead cell
                if board[r][c] == 0 and neighbors_number(board, r, c) == 3:
                    new_board[r][c] = 1
                #for alive cell
                if board[r][c] == 1 and (neighbors_number(board, r, c) < 2 or neighbors_number(board, r, c) > 3):
                    new_board[r][c] = 0
        board = new_board
        print(board)
    return board


                           
if __name__ == "__main__":
    main()