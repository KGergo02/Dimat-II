from math import factorial
def feltolt(halmaz, neve):
    global aub
    global auc
    global aubuc
    global buc
    if neve == 'A':
        num = int(input("A = "))
        halmaz.add(num)
        num = int(input("A U B = "))
        aub = num * -1
        halmaz.add(aub)
        num = int(input("A U C = "))
        auc = num * -1
        halmaz.add(auc)
        num = int(input("A U B U C = "))
        aubuc = num
        halmaz.add(aubuc)
    if neve == 'B':
        num = int(input("B = "))
        halmaz.add(num)
        num = int(input("B U C = "))
        buc = num * -1
        halmaz.add(buc)
        halmaz.add(aub)
        halmaz.add(aubuc)
    if neve == 'C':
        num = int(input("C = "))
        halmaz.add(num)
        halmaz.add(auc)
        halmaz.add(aubuc)
        halmaz.add(buc)


aub = 0
auc = 0
aubuc = 0
buc = 0

A = set()
B = set()
C = set()

print("[1. Feladat]")

n = int(input("Add meg a gyanusitottak szamat: "))

feltolt(A, 'A')
feltolt(B, 'B')
feltolt(C, 'C')

print(f"1. Feladat válasza: {n - sum(A | B | C)}")

print("\n[2. feladat]")

x = int(input("x egyutthatoja = "))

b = int(input("b (ez a zarojelben a szam) = "))

n = int(input("n (zarojel hatvanya) = "))

k = n - x

print(f"{str(factorial(10) // (factorial(2) * factorial(10 - 2)))}*{'(' + str(b) + ')' if b < 0 else b }^{k}")