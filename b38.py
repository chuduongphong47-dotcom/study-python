a = int(input())
b = int(input())
ucln = 1
def ktra(a, b):
    for i in range(1, a + 1):
        if a % i ==0 and b % i == 0:
           ucln = i

    if ucln == 1:
        print("Dung")
    else:
        print("Sai")
ktra(a, b)