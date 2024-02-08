w = list(str(input()))
wr = w[::-1]

i = 0
temp = []
while True:
    temp.append(w[i])
    final = temp + wr
    finalr = final[::-1]
    i += 1
    if final == finalr:
        break

print(''.join(final))
