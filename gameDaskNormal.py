import sys
import dask
import numpy as np
import dask.array as da
from dask.distributed import Client

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
    try:
        chunk_size = int(sys.argv[4])
    except:
        sys.exit(f"Entered value is not a nuber {sys.argv[4]}") 
        
    board = read_input_file(input_name, chunk_size)
    final_board = play_game(board, n)
    write_output_file(output_name, final_board)
          
def read_input_file(input_file, chunk_size):
    # initialize board
    with open(input_file) as f:
        w, h = [int(x) for x in next(f).split()]
        # use the smallest data type
        board = np.zeros((w, h),dtype=np.uint8)
        for line_count, line in enumerate(f, start=0):
            single_numbers = line.split()
            x, y = map(int, single_numbers[:2])
            board[x][y] = 1
        dask_board = da.from_array(board, chunks=(chunk_size, chunk_size))
    return dask_board
                

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
    

def neighbors_number(board, row, col):
    # add plus two to create a proper iteration
    neighbors = board[max(0, row-1):min(board.shape[0], row+2), max(0, col-1):min(board.shape[1], col+2)]
    return np.sum(neighbors) - board[row, col]

def tick(board):
    # the copy takes a lot of space
    w, h = board.shape
    new_board = np.zeros((w, h),dtype=np.uint8)
    for r in range(w):
        for c in range(h):
            #for dead cell
            if board[r][c] == 0 and neighbors_number(board, r, c) == 3:
                new_board[r][c] = 1
            #for alive cell
            if board[r][c] == 1 and (neighbors_number(board, r, c) < 2 or neighbors_number(board, r, c) > 3):
                new_board[r][c] = 0
    return new_board

def play_game(dask_board, iterations):
    for i in range(iterations):
        dask_board = dask_board.map_overlap(tick, depth=1, boundary='none')
    final_board = dask_board.compute()
    return final_board


                           
if __name__ == "__main__":
    client = Client(n_workers=6, threads_per_worker=4, processes=True, memory_limit='2.5GB')
    main()
    client.shutdown()