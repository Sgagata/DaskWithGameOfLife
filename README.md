# Dask with Game of Life
This is an implementation of Conway's Game of life

## Description
The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead (or populated and unpopulated, respectively). 

Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. 

At each step in time, the following transitions occur:

* Any **live** cell with *fewer than two* live neighbours dies, as if by underpopulation.
* Any **live** cell with *two or three* live neighbours lives on to the next generation.
* Any **live** cell with *more than three* live neighbours dies, as if by overpopulation.
* Any **dead** cell with *exactly three* live neighbours becomes a live cell, as if by reproduction.

## Summary

* Any live cell with two or three live neighbours survives.
* Any dead cell with three live neighbours becomes a live cell.
* All other live cells die in the next generation. Similarly, all other dead cells stay dead.

## User input
---
It will be read from the text file

* width and heigh of the grid as unsigned int with space as separation
* **All the other lines:** text input of where a the live cells located as first row number and then column number, as unsigned ints with space as separation
    1. The position is based on zero indexing
    2. Top left is cell is 0 0
    3. Horizontal increases from left to right
    4. Vertical increases from top to bottom

## Implementation
* Get input file name and no of generations as arguments
* load initial pattern of the grid from the input file
* aply the rules for the no of generations
* store the final grid in the output file