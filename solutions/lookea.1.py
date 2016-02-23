fn = input("Enter the filename: ")
inf = open(fn, "r")
outf = open("lookea.1s.txt", "w")

for word in inf:
    res = 0
    for i in range(len(word)):
        char = word[i]
        if char == "a":
            res += 2
        elif char == "d":
            res -= 1
        elif char == "m":
            res = 2 * res
        elif char == "o":
            outf.write(str(res)+"\n")
            break

inf.close()
outf.close()
