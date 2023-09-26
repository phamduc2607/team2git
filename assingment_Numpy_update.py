import tkinter as tk
from tkinter import END, Scrollbar, Text, messagebox

import numpy as np


# Hàm tạo ma trận ngẫu nhiên
def generate_random_matrix():
    mat = np.random.randn(3, 4)
    result_text.insert(END, "Ma trận ngẫu nhiên kích thước 3x4:\n")
    result_text.insert(END, str(mat) + "\n\n")

# Hàm tính giá trị trung bình của vector ngẫu nhiên
def calculate_mean():
    a = np.random.randint(1000, size=(30))
    mean_value = a.mean()
    result_text.insert(END, "Vector ngẫu nhiên kích thước 30:\n")
    result_text.insert(END, str(a) + "\n")
    result_text.insert(END, "Giá trị trung bình của vector là: " + str(mean_value) + "\n\n")

# Hàm chèn số vào mảng NumPy và thay đổi hình dạng
def reshape_array():
    mat = np.random.randint(100, size=(10, 10))
    result_text.insert(END, "Ma trận ngẫu nhiên kích thước 10x10:\n")
    result_text.insert(END, str(mat) + "\n\n")

# Hàm tìm giá trị nhỏ nhất và lớn nhất trong ma trận ngẫu nhiên
def find_min_max():
    mat = np.random.randn(3, 4)
    result_text.insert(END, "Ma trận ngẫu nhiên kích thước 3x4:\n")
    result_text.insert(END, str(mat) + "\n")
    result_text.insert(END, "Giá trị nhỏ nhất trong ma trận là: " + str(np.min(mat)) + "\n")
    result_text.insert(END, "Giá trị lớn nhất trong ma trận là: " + str(np.max(mat)) + "\n\n")

# Hàm tính tích vô hướng của hai mảng
def calculate_dot_product():
    f = np.array([1, 2])
    g = np.array([4, 5])
    dot_product = np.dot(f, g)
    result_text.insert(END, "Mảng thứ nhất: " + str(f) + "\n")
    result_text.insert(END, "Mảng thứ hai: " + str(g) + "\n")
    result_text.insert(END, "Tích vô hướng của hai mảng là: " + str(dot_product) + "\n\n")
def reset_result():
    result_text.delete(1.0, END)

# Tạo cửa sổ giao diện
window = tk.Tk()
window.title("Ứng dụng NumPy")

# Tạo các nút chức năng
generate_matrix_button = tk.Button(window, text="Tạo Ma trận Ngẫu nhiên", command=generate_random_matrix)
calculate_mean_button = tk.Button(window, text="Tính Giá trị Trung bình", command=calculate_mean)
reshape_array_button = tk.Button(window, text="Chèn số vào Mảng", command=reshape_array)
find_min_max_button = tk.Button(window, text="Tìm Min và Max", command=find_min_max)
calculate_dot_product_button = tk.Button(window, text="Tính Tích Vô hướng", command=calculate_dot_product)
reset_button = tk.Button(window, text="Reset", command=reset_result)

# Tạo ô văn bản để hiển thị kết quả
result_text = Text(window, wrap="word", height=15, width=50)
result_text_scrollbar = Scrollbar(window, command=result_text.yview)
result_text.config(yscrollcommand=result_text_scrollbar.set)

# Đặt vị trí các phần tử trên cửa sổ
generate_matrix_button.pack()
calculate_mean_button.pack()
reshape_array_button.pack()
find_min_max_button.pack()
calculate_dot_product_button.pack()
reset_button.pack()
result_text.pack()
result_text_scrollbar.pack(side="right", fill="y")

# Chạy ứng dụng
window.mainloop()
