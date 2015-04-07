# Python program that returns all the possible unique games given a board size n and
# number of turns t. You roll a 3-sided dice, "Stay","Right","Left" . You start at the leftmost
# square on the board, and the goal is reach the rightmost square of the board in t turns.
# There are 3 rules:
# 1. If you are the leftmost block on the board you cannot move left, ony right or stay. 
# 2. If you are anywhere in the middle you can move left, right, or stay.
# 3. If you reach the rightmost block before the number of turns your only option is to stay.

def recursive(t,n,s):
	g = 0
	if t == 0:
		return 1 if s == n else 0
	g += recursive(t-1,n,s)
	if s+1<= n and s+1>= 0:
		g += recursive(t-1,n,s+1)
	if s < n and s-1 >= 0:
		g += recursive(t-1,n,s-1)
	return g

# Uses a 2xn array to represent a memo table.
# Going to use dyanmic programming to build a table where each
# cell represents the number of possible moves at the given block and time
# The length of the array is the number of number of blocks in the board
# t is the number of moves allowed
def dynamic(t,n,m):
	pre = m[0] # Split the 2xn array into 2 n-size array for easier access
	cur = m[1]

	for c in range(t+1):
		for r in range(n):
			# At time t = 0, no moves are possible to win
			if c==0:
				cur[r] = 0
			# At any other time 0 < t the number of possible depends on the
			# previous cells in the table
			if c > 0:
				# Can only go forward or stay
				if r == 0:
					cur[r] = pre[r] + pre[r+1]
				# Otherwise can go forward, stay, or back
				elif r < n-1:
					cur[r] = pre[r] + pre[r+1] + pre[r-1]
			# When reached the leftmost block, only option is to stay, thus
			# num of moves is just 1
			if r == n-1:
				cur[r] = 1
		# To save memory set pre as cur and cur as an array of 0
		pre = cur
		cur = [0]*n
	return pre[0]

def answer(t,n):

	table = [[0 for x in range(n)] for x in range(2)] # creates an 2 2xn arrays initialized to 0
	print(dynamic(t,n,table))

answer(100,7)