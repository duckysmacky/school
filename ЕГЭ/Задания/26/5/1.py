file = open("26_14733.txt")
# file = open("test")
n = int(file.readline())
favs = []
other = []
for line in file:
    start, length, fav = map(int, line.split())
    end = start + length 
    song = (end, start, fav)
    if fav == 1:
        favs.append(song)
    else:
        other.append(song)

favs.sort()
other.sort()
playlist = []

for end, start, fav in favs:
    playlist.append((start, end, fav))
playlist.sort()

for end, start, fav in other:
    for i in range(len(playlist) - 1):
        if start >= playlist[i][1] and end <= playlist[i + 1][0]:
            playlist.insert(i + 1, (start, end, fav))
            break
print(playlist[-6:])
# print(other)
print(max([e for e, s, f in other if s >= 99730 and e <= 101193]))
print(len(playlist))
# 109 102941
