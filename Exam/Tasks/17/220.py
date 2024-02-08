# ((z → y) ∧ (¬ x → w)) → ((z ≡ w) ∨ (y ∧ ¬ x))
# ((z <= y) and ((not x) <= w)) <= ((z == w) and (y and (not x)))

r = range(2)

for w in r:
    for y in r:
        for z in r:
            for x in r:
                if ((z <= y) and ((not x) <= w)) <= ((z == w) and (y and (not x))) == 0:
                    print(w, y, z, x) # wyzx