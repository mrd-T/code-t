import numpy as np

# 定义矩阵 A
A = np.array([[5, -1, 1],
              [-1, 2, 0],
              [1, 0, 3]])

# 计算特征值
eigenvalues = np.linalg.eigvals(A)

# 计算特征值的绝对值
abs_eigenvalues = np.abs(eigenvalues)

# 找到最大和最小特征值
lambda_1 = abs_eigenvalues[0]
lambda_2 = abs_eigenvalues[1]
lambda_3 = abs_eigenvalues[2]

# 计算比率
ratio = lambda_1 / lambda_3

print(f'特征值: {abs_eigenvalues}')
print(f'Ratio of |lambda_1| / |lambda_3|: {ratio}')
