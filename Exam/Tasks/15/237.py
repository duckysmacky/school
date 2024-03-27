D = range(133, 178)
B = range(144, 191)

m = 10 ** 10

for a in range(1, 500):
    for b in range(a, 500):
        A = range(a, b)
        found = True
        for x in range(1, 10_000):
            # (x ∈ D) -> (((x ∈ B) ∧ !(x ∈ A)) -> !(x ∈∨ D))
            if not (x in D) or (not (not (x in B) and not (x in A)) or not (x in D)): continue
            found = False
            break
        if found:
            m = min(m, len(A))
            break
print(m, A)
# >45
