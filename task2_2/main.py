import numpy as np
import nashpy as nash
import re
import matplotlib.pyplot as plt

print("Введите количество строк матрицы H")
n = int(input())
H = []
for i in range(n):
    print("Введите элементы " + str(i+1)+" строки через пробел")
    H.append([int(j) for j in input().split()])
row_del = []
col_del = []
alpha = []
for i in range(n):
    alpha.append(min(H[i]))
a = max(alpha)
beta = []
h = np.array(H)
for i in range(len(H[0])):
    beta.append(max(h[:,i]))
b = min(beta)
print("a =", a)
print("b =", b)
H_np = np.array(H)
rps = nash.Game(H_np)
equilibria = rps.support_enumeration()
string = str(list(equilibria))
variance = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?',string)
p = variance[:n]
q = variance[n:(n+len(H[0]))]
for_I = []
for_J = []
for i in range(len(p)):
    if p[i] == '0.':
        row_del.append(i)
    else:
        for_I.append(int(i))
for j in range(len(q)):
    if q[j] == '0.':
        col_del.append(j)
    else:
        for_J.append(int(j))
row_del = row_del[::-1]
col_del = col_del[::-1]
for row in row_del:
    H_np  = np.delete(H_np, (row), axis=0)
for col in col_del:
    H_np  = np.delete(H_np, (col), axis=1)
I = 0.
H_np_trans = H_np.transpose()
for i in range(len(H_np_trans[0])):
    I = I + H_np_trans[0][i]*float(p[for_I[i]])
print("Значение игры:", I)
print("Для первого игрока:")
print("p =",p)
print("Для второго игрока:")
print("q =",q)
H_np_trans = H_np.transpose()
plt.subplot(211)
plt.plot([0,1],[H_np[1][0], H_np[0][0]],[0,1],[H_np[1][1], H_np[0][1]])
plt.xlim(0,1)
plt.title("Первый игрок")
plt.annotate(
    'Точка пересечения, I = ' + str('{0:.3f}'.format(I)),
    (float(p[for_I[0]]), I),
    xytext=(float(p[for_I[0]])+0.1, I+0.3),
    arrowprops={
        'facecolor': 'black',
        'shrink': 0.05
    }
)
plt.subplot(212)
plt.plot([0,1],[H_np[0][1], H_np[0][0]],[0,1],[H_np[1][1], H_np[1][0]])
plt.xlim(0,1)
plt.title("Второй игрок")
plt.annotate(
    'Точка пересечения, I = ' + str('{0:.3f}'.format(I)),
    (float(q[for_J[0]]), I),
    xytext=(float(q[for_J[0]])+0.1, I+0.3),
    arrowprops={
        'facecolor': 'black',
        'shrink': 0.05
    }
)
plt.show()
