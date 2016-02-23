fn = input("Enter the filename: ")
inf = open(fn, "r")
outf = open("lookea.6s.txt", "w")

for word in inf:
    n = 2
    n3 = 0
    n2 = 1
    n1 = 1

    sum = 0

    while n < int(word):
        if n % 3 == 0:
            sum += n
        n3 = n2
        n2 = n1
        n1 = n
        n = n3 + n2 + n1
    
    outf.write(str(sum)+"\n")

inf.close()
outf.close()
