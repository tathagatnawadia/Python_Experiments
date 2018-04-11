'''
Instead of using for loop to create
[0 0 0 0 0 0]
call
[0] * 6 

This is a lot faster
but 
[[]] * 5 
arr[0].append(1)
[[1], [1], [1] ... ]
This doesnt work for complex objects 

for achieving this use numpy
np.zeros(1000)
'''

