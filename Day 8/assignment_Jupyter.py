import numpy as np

# Creating 1 D array
arr_1d = np.array([1, 2, 3, 4])
print("1D Array: ", arr_1d)

# Creating 2D array
arr_2d = np.array([[1,2,3], [4,5,6]])
print("2D array: ", arr_2d)
np.ndim(arr_2d)

# Creating 3D array
arr_3d = np.array([[[1,2],[3,4],[5,6],[7,8]]])
print("3D array: ", arr_3d)

np.ndim(arr_3d)

# Creating an array of ones
ones = np.ones((3,2))


# Creating an array of zeroes
zeros = np.zeros((2,2))

# Creating a 2x2 array filled with the value 7
full_array = np.full((2,2), 7)

# Creating an array with values from 0 to 9
range_arr = np.arange(0, 10)
print(range_arr)

# Creating an array with values from 0 to 19 with a step of 3
step_arr = np.arange(0, 20, 3)
print(step_arr)

# Creating an array with linearly spaced values
linspace_arr = np.linspace(0, 1, 10)
print(linspace_arr)

# Creating a 3x3 array with random values
random_array = np.random.rand(3, 3)
random_array

# Creating a 3x3 array with random integer values between 1 to 10
random_int = np.random.randint(1, 10, size=(3,3))
random_int

# Creating an 3x3 identity matrix
identity_matrix = np.eye(3)
identity_matrix

diag_mat = np.diag([1,2,3,4])
diag_mat

arr = np.array([1,2,3,4,5, 0])
arr

# Reshaping a 1D array to 2D array
arr = arr.reshape((2,3))
arr

empty_1d = np.empty(5)
empty_1d

empty_2d = np.empty((3,3))
empty_2d

empty_3d = np.empty((3,3,3))
empty_3d

empty_int = np.empty((2,2), dtype = int)
empty_int



array1d=np.array([1,2,3])

array1d.ndim


array1d.shape

array1d.size

array1d.dtype

array1d.nbytes

array1d.itemsize



array2d=np.array([[1,2,3,5,6],[6,7,8,9,10],[11,12,13,14,15]])
sliced_array=array2d[::1, ::2]
print(sliced_array)


# Access every 2nd row and 2nd column and every 2nd layer in 3D array
a3 = np.array([[[1,2,3], [4,5,6], [7,8,9]],
              [[10,11,12], [13,14,15], [16,17,18]],
              [[19,20,21], [22,23,24], [25,26,27]] ])


a3[::1, ::1, ::1]



