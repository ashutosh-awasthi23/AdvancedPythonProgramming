import numpy as np
arr1= np.random.randint(1,10,(4,2))
arr2= np.random.randint(1,10,(2,3))
arr3=np.matmul(arr1,arr2)
print(f"The matrices are \n{arr1} and \n{arr2}")
print(f"The multiplication of two matrices came out to be\n{arr3}")
print(f"The transpose of the resultant matrix is \n{arr3.T}")
