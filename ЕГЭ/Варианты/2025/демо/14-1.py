for x in "0123456789ABCDEFGHI":
    val = int(f"98897{x}21", 19) + int(f"2{x}923", 19)
    if val % 18 == 0:
        print(x, val / 18)
