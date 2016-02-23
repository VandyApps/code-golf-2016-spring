fn = input("Enter the filename: ")
inf = open(fn, "r")
outf = open("lookea.5s.txt", "w")

for word in inf:
    val = int(word)
    res = "o\n"

    while val != 0:
        if val % 2 == 1:
            val += 1
            res = "d" + res
        elif (val/2)%2==0 or val < 0:
            val = val / 2
            res = "m" + res
        else:
            val -= 2
            res = "a" + res

    outf.write(res)

inf.close()
outf.close()
