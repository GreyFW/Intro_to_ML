import numpy as np

def solving_2on2_linear(a11, a12, a21, a22, b1, b2):
    A = np.array([[a11, a12],
                 [a21, a22]], dtype=float)
    b = np.array([b1, b2], dtype=float)
    
    det=np.linalg.det(A)
    eps = 1e-12
    if abs(det) < eps:
        print("Существует бесконечное мн-во решений, либо ни одного решения.")
        return 0, 0
    else:
        x, y = np.linalg.solve(A, b)
        return(x, y)

def main():
    print(f"Введите коэффициенты a11, a12, a21, a22, b1, b2:")
    a11, a12, a21, a22, b1, b2 = map(float, input().split())
    x, y = solving_2on2_linear(a11, a12, a21, a22, b1, b2)
    if x == y == 0:
        return
    print(x, y)
    
main()