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
print "Your first matrix is", amatrix
print "Your second matrix is", bmatrix
def multiply(amatrix, bmatrix):
	if len(amatrix[0]) != brow:
		return "You can't multiply these." #makes sure that the matrices are able to be multiplied based on their dimensions
	multiplied_matrix = []
	x = 0 #each of these variables represents horizontal and vertical dimensions for each of the two matrices
	y = 0
	z = 0
	w = 0
	row = []
	numbers = []
	while y < brow:
		numbers.append(amatrix[x[y]] * bmatrix[z[w]])
		z = z+1
		y = y+1
		#supposed to multiply the the numbers that will create the first element in the multiplied matrix
	numbers = []
	while len(row) < brow:
		element = sum(numbers)
		row.append(element)
		#this makes the row of the multiplied matrix by putting all the elements in a list
	multiplied_matrix.append(row)


