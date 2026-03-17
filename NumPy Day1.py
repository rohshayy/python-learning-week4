
import numpy as np

#print(np.__version__)
'''
my_list = [1, 2, 3, 4, 5, 6]
print(my_list)

my_array = np.array([1, 2, 3, 4, 5, 6])
print(my_array)
print(type(my_array))
my_array = my_array * 2
print(my_array)

'''
'''
array =np.array('A')
print(array.ndim)



array =np.array(['A' , 'B' , 'C' , 'D' , 'E' , 'F'])
print(array.ndim)

array =np.array([['A' , 'B' , 'C'],
                ['D' , 'E' , 'F']])
print(array.ndim)

array =np.array([[['A' , 'B' , 'C'],['D' , 'E' , 'F'], ['G' , 'H' , 'I']],
                 [['J' , 'K' , 'L'],['M' , 'N' , '0'], ['P' , 'Q' , 'R']],
                 [['S' , 'T' , 'U'],['V' , 'W' , 'X'], ['Y' , 'Z' , ' ']]])
print(array.ndim)
print(array.shape)
print(array.size)

print(array[0][0][0])
print(array[0,0,0])
word = array[0,0,0] + array[2,0,0]
print(word)
'''
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix)
print(matrix.ndim)
print(matrix[0,1])
