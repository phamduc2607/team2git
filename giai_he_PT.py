import numpy as np

def solve_linear_equations(coefficients, constants):
    try:
        A = np.array(coefficients)
        B = np.array(constants)
        A_inv = np.linalg.inv(A)
        X = np.dot(A_inv, B)
        return X
    except np.linalg.LinAlgError:
        return None

def main():
    num_equations = int(input("Nhập số lượng phương trình: "))
    num_unknowns = int(input("Nhập số lượng ẩn: "))

    coefficients = []
    constants = []

    print("Nhập hệ số các phương trình:")
    for i in range(num_equations):
        equation = []
        for j in range(num_unknowns):
            coefficient = float(input(f"Nhập hệ số của ẩn x{j+1} trong phương trình {i+1}: "))
            equation.append(coefficient)
        coefficients.append(equation)

        constant = float(input(f"Nhập hệ số tự do trong phương trình {i+1}: "))
        constants.append(constant)

    solution = solve_linear_equations(coefficients, constants)

    if solution is not None:
        print("Nghiệm của hệ phương trình:")
        for i, value in enumerate(solution):
            print(f"x{i+1} = {value}")
    else:
        print("Hệ phương trình vô nghiệm hoặc vô số nghiệm.")

if __name__ == "__main__":
    main()