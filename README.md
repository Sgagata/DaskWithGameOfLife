# Dask with Game of Life
This is an implementation of Conway's Game of life

## Description
The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead (or populated and unpopulated, respectively).Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

* Any **live** cell with *fewer than two* live neighbours dies, as if by underpopulation.
* Any **live** cell with *two or three* live neighbours lives on to the next generation.
* Any **live** cell with *more than three* live neighbours dies, as if by overpopulation.
* Any **dead** cell with *exactly three* live neighbours becomes a live cell, as if by reproduction.

## Summary

* Any live cell with two or three live neighbours survives.
* Any dead cell with three live neighbours becomes a live cell.
* All other live cells die in the next generation. Similarly, all other dead cells stay dead.

## User input

The Initial living cells will be read from the text file

* **The first line** line of the text file indicates the width and heigh of the grid as unsigned int with space as separation
* **All the other lines:** text input of where a the live cells located as first row number and then column number, as unsigned ints with space as separation
    1. The position is based on **zero indexing**
    2. Top left cell is 0 0
    3. **Horizontal Index** increases from left to right
    4. **Vertical Index**increases from top to bottom

## Implementation
* Get input file name and no of generations as arguments
* Load initial pattern of the grid from the input file
* For Dask implementation - the grid will be splitted into a number of Dask Array and function will be used (**Map_Overlay**) to    share an identical block between splitted grids.  
* Aply the rules for the no of generations
* Store the final grid in the output file

## Script Implementation Guideline
To explore several benchmarks for grids, we have applied several scripts for this task. Some srcipts are in Python text file and some are in Jupyter Notebook.
* **Jupyter Notebook** - Change the input and output file directory and put number of generations.
* **Python Files for Dask** - To run python files you can follow (<file.py> Input name with directory> Output name and Saving Directory> number of iterations> Chunk Size) this in your terminal
* **Python Files Without Dask** - To run python files you can follow ((<file.py> Input name with directory> Output name and Saving Directory> number of iterations) this in your terminal
 