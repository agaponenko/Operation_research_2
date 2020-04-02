from scipy.optimize import linprog
import numpy as np
print("Введите количество строк матрицы H:")
n = int(input())
H = []
for i in range(n):
    print("Введите элементы " + str(i+1) + " строки через пробел:")
    H.append([int(j) for j in input().split()])
alpha = []
for i in range(n):
    alpha.append(min(H[i]))
a = max(alpha)
beta = []
h = np.array(H)
for i in range(len(H[0])):
    beta.append(max(h[:,i]))
b = min(beta)
if(a == b):
    print("Разрешима в чистых стратегиях.")
else:
    print("Не разрешима в чистых стратегиях.")
x = [1 for i in range(n)]
A_ub = np.array(H).transpose()*(-1)
b_ub = [-1 for i in range(len(H[0]))]
x_solve = linprog(x, A_ub, b_ub).x
print ("x =", x_solve)
y = [-1 for i in range(len(H[0]))]
A_ub = H
b_ub = [1 for i in range(n)]#'1'
y_solve = linprog(y, A_ub, b_ub).x
print("y =", y_solve)
I = 1/sum(y_solve)
print ("Значение игры :", I)
p = [I*variable for variable in x_solve]
print("p =", p)
q = [I*variable for variable in y_solve]
print("q =", q)