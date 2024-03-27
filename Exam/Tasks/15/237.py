# TODO

def search(start, end):
    D = range(133, 178)
    B = range(144, 191)

    A = range(start, end)
    for _ in A:
        found = True
        for x in range(1, 200):
            # (x ∈ D) -> ((!(x ∈ B) ∧ !(x ∈ A)) -> !(x ∈ D))
            if (not (x in D) or (not (not (x in B) and not (x in A)) or not (x in D))) == 1: continue
            found = False
            break
        if found: return True

    return False

end_pos = 300
while search(1, end_pos):
    print(f"End: {end_pos}")
    end_pos -= 1

start_pos = 1
while search(start_pos, 300):
    print(f"Start: {start_pos}")
    start_pos += 1

print(f"Answer: {end_pos - start_pos}")
# >45
