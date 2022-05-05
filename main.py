import numpy as np
import math

def zadanie3(n):
    n = int(n)
    tab = np.arange(1, n * n, 1)
    return (tab)

def zadanie4(a4, b4):
    c4 = np.logspace(1, b4, num = b4, dtype = int, base = a4)
    print(c4)

def zadanie5(a5):
    c5 = np.arange(a5)
    c5 = np.flip(c5)
    d5 = np.diag(c5)
    print(d5)

def zadanie7(a7):
    b7 = np.arange(a7)
    d7 = np.arange(2, b7.size * 2 + 1, 2)
    d7_flipped = np.flip(d7)
    print(d7)
    print(d7_flipped)
    for i in b7:
        b7[i] = 2
    c7 = np.diag(b7)
    for x in range(0, d7.size, 1):
        was_equal = 0
        for y in range(0, d7.size, 1):
            if x == y:
                was_equal = 1
                continue
            if was_equal == 1 and x != y:
                c7[x][y] = d7[y - x]
                c7[y][x] = d7_flipped[x - y - 1]
    print(c7)

def zadanie9(a9, b9, i, tab):
    a3 = a9 + b9
    tab[i] = a3
    if a3 > 120000:
        return a3
    return zadanie9(b9, a3, i + 1, tab)

print("Zadanie 1")
a = np.arange(3, 48, 3)
print("a = ", a)
print("\nZadanie 2")
a = np.array([8.5654666, 1.345, 0.6788, 34.3212, 3.1415, 2.618])
b = a.astype('int64')
print(b)
print("\nZadanie 3")
print(zadanie3(8))
print("\nZadanie 4")
zadanie4(2, 4)
print("\nZadanie 5")
zadanie5(4)
print("\nZadanie 6")
a = np.array([[1, 1, 1], [1, 0, 0], [1, 1, 1], [0, 0, 1], [1, 1, 1]])
print(a)
print("\nZadanie 7")
zadanie7(3)
print("\nZadanie 9")
tab = np.arange(25)
zadanie9(0, 1, 0, tab)
print(tab)
a9 = np.arange(5)
b9 = np.diag(a9)
j = 0
for x in range(0, a9.size, 1):
    for y in range(0, a9.size, 1):
        b9[x][y] = tab[j]
        j = j + 1
print("\ntablica 5x5 z kolejnymi liczbami ciagu Fibonacciego:")
print(b9)