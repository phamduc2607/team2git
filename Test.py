import numpy as np

# k tao ma tran
A = np.zeros((2, 2))
B = np.zeros(2)

print("Nhap a")
k=0;
for i in range(2):
    for j in range(2):
        k+=1;
        A[i][j] = float(input(f"A[{k}] = "))
print("Nhap B:")
for i in range(2):
    B[i] = float(input(f"B{i+1} = "))

# giai he pt
A_inv = np.linalg.inv(A)
X = np.dot(A_inv, B)

print('Nghiem la:')
for i in range(2):
    # ket qua lam tron den chu so thap phan thu 2
    print(f'x{i+1} = {X[i]:.2f}')
import numpy as np

# Nhập số lượng phương trình và ẩn từ người dùng
n = int(input("Nhập số lượng phương trình: "))
m = int(input("Nhập số lượng ẩn: "))

# k tao ma tran
A = np.zeros((n, m))
B = np.zeros(n)

print("Nhap A:")
k = 0
for i in range(n):
    for j in range(m):
        k += 1
        A[i][j] = float(input(f"A[{k}] = "))

print("Nhap B:")
for i in range(n):
    B[i] = float(input(f"B[{i + 1}] = "))

# Kiểm tra rank của ma trận A và ma trận mở rộng [A|B]
augmented_matrix = np.column_stack((A, B))
rank_A = np.linalg.matrix_rank(A)
rank_augmented = np.linalg.matrix_rank(augmented_matrix)

if rank_A == rank_augmented == m:
    X = np.linalg.solve(A, B)
    print('Nghiem cua he phuong trinh: ')
    for i in range(m):
        print(f'x{i + 1} = {X[i]:.2f}')
elif rank_A == rank_augmented < m:
    print('Vo so nghiem.')
else:
    print('vo nghiem')