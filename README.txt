# Python program that returns all the possible unique games given a board size n and
# number of turns t. You roll a 3-sided dice, "Stay","Right","Left" . You start at the leftmost
# square on the board, and the goal is reach the rightmost square of the board in t turns.
# There are 3 rules:
# 1. If you are the leftmost block on the board you cannot move left, ony right or stay. 
# 2. If you are anywhere in the middle you can move left, right, or stay.
# 3. If you reach the rightmost block before the number of turns your only option is to # stay.

USAGE:
# Uses a 2xn array to represent a memo table.
# Going to use dyanmic programming to build a table where each
# cell represents the number of possible moves at the given block and time
# The length of the array is the number of number of blocks in the board and
# t is the number of moves allowed

# Visualization:

Given a board of size 3, n, with only 5 moves allowed

moves:	   0	   1	   2	   3	    4	    5	   ..      ..
	-----------------------------------------------------------------
pos:1	|   0	|   0	|   1	|   3	|   7	|   15	|	|	|
pos:2	|   0	|   1	|   2	|   4	|   8	|   16	|	|	|
pos:3	|   1	|   1	|   1	|   1	|   1	|    1	|	|	|
pos:	|   	|   	|   	|   	|   	|    	|	|	|
pos:	|   	|   	|   	|	|	|	|	|	|
pos:	|   	|   	|   	|	|	|	|	|	|
pos:	|	|	|	|	|	|	|	|	|
pos:	|	|	|	|	|	|	|	|	|
pos:	|	|	|	|	|	|	|	|	|
pos:	|	|	|	|	|	|	|	|	|
pos:	|	|	|	|	|	|	|	|	|
pos:	|	|	|	|	|	|	|	|	|
pos:	|	|	|	|	|	|	|	|	|

at position 0, with 0 moves, there are 0 possible moves
.
.
.
.
same for entire column 0 since there are no possible moves that can win
EXCEPT for at position 5, since at position 5 you are already the left-most block.

For any other time t , 0 < t < moves, the number of possible moves is the sum of possible moves if you stay, go back, or forward.

Since at the beginning of the game we start at position 1, by looking at the table, the number of possible games starting at position 1 with 5 moves allowed is 15, aka always the top right most cell.