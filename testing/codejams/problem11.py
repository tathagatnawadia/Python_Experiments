m = 5
n = 5 
k = 2
r = 1
X = [1,3]
Y = [3,3]

print(m,n,k,r,X,Y)

def checkCordinates(x, y):
	if x < m and y < n and x >= 0 and y >= 0:
		return True
	else:
		return False

def makePixelsDead(x, y, user_map):
	if(checkCordinates(x, y)):
		user_map[x][y] = 0

def deadCircles(x, y, r, user_map):
	makePixelsDead(x, y, user_map)
	makePixelsDead(x, y+r, user_map)
	makePixelsDead(x, y-r, user_map)
	makePixelsDead(x-r, y, user_map)
	makePixelsDead(x-r, y+r, user_map)
	makePixelsDead(x-r, y-r, user_map)
	makePixelsDead(x+r, y, user_map)
	makePixelsDead(x+r, y+r, user_map)
	makePixelsDead(x+r, y-r, user_map)

user_map = [[1 for x in range(m)] for y in range(n)]

for i in range(0,k):
	deadCircles(X[i]-1, Y[i]-1, r, user_map)

print(user_map)