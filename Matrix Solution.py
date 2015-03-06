print "Please enter how many rows your first matrix has."
arow = int(raw_input()) #arow is how many rows the first matrix has
n = 0
amatrix = []
while n < arow:
	if n == 0:
		print "Please enter the first row with commas in between the numbers: "
		arow_input = raw_input()
	else:
		print "Please enter the next row with commas in between the numbers: "
		arow_input = raw_input() #arow_input is each row.
	amatrix.append([int(num) for num in arow_input.split(",")]) #takes each arow_input, splits the numbers, and puts them in a list inside the amatrix list
	n = n + 1
print "Please enter how many rows your second matrix has."
brow = int(raw_input()) #all this is the same, but for the second matrix
n = 0
bmatrix = []
while n < brow:
	if n == 0:
		print "Please enter the first row with commas in between the numbers: "
		brow_input = raw_input()
	else:
		print "Please enter the next row with commas in between the numbers: "
		brow_input = raw_input()
	bmatrix.append([int(num) for num in brow_input.split(",")])
	n = n + 1

def multiply(a, b):
	if len(amatrix[0]) != brow:
		return "impossible." #makes sure that the matrices are able to be multiplied based on their dimensions
	multiplied_matrix = []
	x = 0 #each of these variables represents horizontal and vertical dimensions for each of the two matrices
	y = 0
	w = 0
	numbers = []
	row = []
	while x < arow:
		while w < len(bmatrix[0]):
			while y < brow:
				mini_element = amatrix[x][y] * bmatrix[y][w]
				numbers.append(mini_element)
				y = y + 1
			row.append(sum(numbers))
			w = w + 1
			y = 0
			numbers = []
		multiplied_matrix.append(row)
		row = []
		x = x + 1
		y = 0
		w = 0
	return multiplied_matrix

print "Your first matrix is", amatrix
print "Your second matrix is", bmatrix
print "Your multiplied matrix is", multiply(amatrix, bmatrix)
