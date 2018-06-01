'''
Given a binary matrix, find out the maximum size square sub-matrix with all 1s.

For example, consider the below binary matrix.
maximum-size-square-sub-matrix-with-all-1s
'''

input_matrix = [[0,1,1,0,1],
				[1,1,0,1,0],
				[0,1,1,1,0],
				[1,1,1,1,0],
				[1,1,1,1,1],
				[1,1,1,1,0]]
print(input_matrix)
R = len(input_matrix)
C = len(input_matrix[0])

interim_matrix = [[0 for i in range(C)] for j in range(R)]
interim_matrix[0] = input_matrix[0] #Copying first row
for i in range(R):
	interim_matrix[i][0] = input_matrix[i][0] #Copying first column

print("R : ", R)
print("C : ", C)

for i in range(1,R):
	for j in range(1,C):
		if input_matrix[i][j] == 1:
			interim_matrix[i][j] = min(interim_matrix[i-1][j],
									interim_matrix[i][j-1],
									interim_matrix[i-1][j-1]) + 1

print(interim_matrix)