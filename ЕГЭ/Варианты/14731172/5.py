N = 0
i = -1
while N <= 52:
    i += 1
    Nb = str(bin(i))
    if i % 2 == 0:
        Nb = "1" + Nb + "0"
        print(Nb, i)
    else:
        Nb = "11" + Nb + "11"
    N = int(Nb.replace("0b", ""), 2)
print(i)