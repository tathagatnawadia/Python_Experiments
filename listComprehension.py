#getting all possible combinations from 1,30 for satisfying the circle formula
circle1 = [(x,y,z) for x in range(1,30) for y in range(1,30) for z in range(1,30) if x**2 + y**2 == z**2]
circle2 = [(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2]
print(circle1)
print(circle2)



#combining lists
colours = ["red", "green", "blue", "black"]
things = ["car", "house", "mobile", "laptop"]
coloured_things = [(color,thing) for color in colours for thing in things]
print(coloured_things)

