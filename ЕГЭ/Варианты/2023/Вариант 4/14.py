from string import ascii_uppercase, digits

alph = digits + ascii_uppercase

for x in alph[:15]:
    val = int(f"82{x}19", 15) - int(f"6{x}073", 15)
    if val % 11 == 0:
        print(val, val // 11)