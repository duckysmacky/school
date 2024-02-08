# (¬a  b) ∧ (b ≡ ¬c) ∧ ¬d
# (not(a) <= b) and (b != c) and not(d)

r = range(2)

for a in r:
    for c in r:
        for b in r:
            for d in r:
                if ((not a) <= b) and (b == (not c)) and (not d) == 1:
                    print(b, a, c, d) # bacd