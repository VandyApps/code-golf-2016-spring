fn = input("Enter the filename: ")
inf = open(fn, "r")
outf = open("lookea.4s.txt", "w")

for word in inf:
    a = word[:-1]
    count = {}
    for i in range(len(a)):
        count[a[i]] = 0
    for i in range(len(a)):
        count[a[i]] += 1
           
    flag = False
    good = True
    for key in count:
        if (count[key] % 2 == 1):
            if flag:
                good = False
                outf.write("no\n")
                break
            flag = True
    if good:
        outf.write("yes\n")

inf.close()
outf.close()
