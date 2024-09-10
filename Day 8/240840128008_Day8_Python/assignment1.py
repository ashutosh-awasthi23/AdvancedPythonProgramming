import numpy as np
arr1=np.random.randint(1,10,(3,3))
eigenvalues,eigenvectors=np.linalg.eig(arr1)
eigenvalues=eigenvalues.reshape(-1,1)
print((eigenvalues))
print(eigenvectors)
# arr2=np.row_stack(eigenvalues,eigenvectors)
# print(arr2)