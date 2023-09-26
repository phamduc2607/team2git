import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('diemPython.csv', index_col=0, header=0)
in_data = array(df.iloc[:, :])

# Extract the total number of students
tongsv = in_data[:, 1]
tongsvabc= in_data[:, [3,5, 7]]
tongsvlonhonD= in_data[:,[3,4,5,6,7,8,9]]
print(tongsvabc)

# Calculate the sum of total students
total_students = np.sum(tongsv)
total_ABC = np.sum(tongsvabc)
total_londonD=np.sum(tongsvlonhonD)

# Create a bar chart
plt.bar("Total Students", total_students)

# Add labels
plt.xlabel("Category")
plt.ylabel("Total Students")
plt.title("Total Students in the Exam")
# Create a bar chart
plt.bar("Total ABC", total_ABC)

# Add labels
plt.xlabel("Category")
plt.ylabel("Total Students")
plt.title("Total Students in the Exam")
plt.bar("Total >=D", total_londonD)

# Add labels
plt.xlabel("Category")
plt.ylabel("Total Students")
plt.title("Total Students in the Exam")

# Show the plot
plt.show()

