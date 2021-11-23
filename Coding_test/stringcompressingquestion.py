s = "aabbaccc"

length = len(s)
slicing_size = 0
find_shortest = []
for i in range(1,length):
    sliced = []
    n = 0
    m = 0
    for j in range(0,int(length/i)+1):
        m += i
        sliced.append(s[n:m])
        n += i
    while '' in sliced:
        sliced.remove('')
    tmp = sliced[0]
    tmp_c = 1
    tmp_l = []
    while sliced:
        if len(sliced) == 1:
            tmp_l.append([tmp,tmp_c])
            break
        if tmp == sliced[1]:
            tmp_c += 1
            sliced.pop(0)
        else:
            tmp_l.append([tmp,tmp_c])
            tmp = sliced[1]
            tmp_c = 1
            sliced.pop(0)
    compressed_strings = ""
    for items in tmp_l:
        if items[1] != 1:
            compressed_strings = compressed_strings + str(items[1])
        compressed_strings = compressed_strings + items[0]
    find_shortest.append(len(compressed_strings))
    print(compressed_strings)
find_shortest.sort()
find_shortest[0]