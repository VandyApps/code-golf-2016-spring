fn = input("Enter the filename: ")
inf = open(fn, "r")
outf = open("lookea.2s.txt", "w")

for word in inf:
    a = int(word)
    while True:
        if (a == 42):
            outf.write("yes\n")
            break
        elif (a < 42):
            outf.write("no\n")
            break

        if (a % 2 == 0):
            a = a / 2
        elif (a % 3 == 0):
            x = a % 10
            y = (a % 100)/10
            a = a - x * y - 1
        elif (a % 5 == 0):
            a = a - 42
        else:
            a = a - 1

inf.close()
outf.close()
