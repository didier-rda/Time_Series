#   importing libs
import numpy as np

#  numoy arrays
my_list = ([1,2,3],[4,5,6],[7,8,9])
my_matrix = np.array(my_list)
my_matrix.shape

#  numpy broadcasting
np.ones((5,5)) + 4
np.linspace(0,10,20)

#  no ident matrix
np.eye(10)

#  random
np.random.rand(5,5)

#  random normal
np.random.randn(10)

#  random int
np.random.randint(1,100)

np.random.seed(42)
np.random.rand(4)

arr = np.arange(25)
arr.shape
arr_reshape = arr.reshape(5,5)
arr_reshape.shape
arr_reshape.argmax()
arr_reshape.argmin()
arr_reshape.dtype

#  indexing and selection
arr = np.arange(0,11)
arr[1:5]

arr + 100
arr
slice_of_arr = arr[0:6]
slice_of_arr[:] = 99
arr
arr_2d = np.array([[5, 10, 15],[20,25,30],[35,40,45]])
arr_2d

arr_2d[:2,1:]
bool_arr2d = arr_2d > 20
arr_2d[bool_arr2d]

#  numpy operations

