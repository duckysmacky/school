def is_triangle(tr):
    return tr[0] + tr[1] > tr[2] \
        and tr[1] + tr[2] > tr[0] \
        and tr[2] + tr[0] > tr[1]

def find_triples(arr):
    triples = []
    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                tr = (arr[i], arr[j], arr[k])
                if is_triangle(tr):
                    triples.append(tr)
    return triples

def find(arr):
    triples = find_triples(arr)
    print(len(triples), len(arr))

a = [14, 10, 13, 13]
b = [1, 6, 7, 5, 2, 3]
c = [1, 2, 7, 3, 7, 3, 8, 9]
d = [1, 2, 7, 8, 7, 1, 7, 8, 8, 10]

for arr in [a, b, c, d]:
    find(arr)
