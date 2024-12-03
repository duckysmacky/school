file = open("Задание 26/26-test.txt")
max_movie_len, participans = map(int, file.readline().split())
lengths = sorted(list(map(int, file.readlines())))

max_cnt = 0
never_in = 0
considered = set()

for i in range(len(lengths)):
    sum_lengths = lengths[i]
    cnt = 0
    for j in range(len(lengths)):
        if j == i: continue
        if sum_lengths <= max_movie_len - lengths[j]:
            sum_lengths += lengths[j]
            cnt += 1
        else:
            break
    if cnt > max_cnt:
        considered.add()