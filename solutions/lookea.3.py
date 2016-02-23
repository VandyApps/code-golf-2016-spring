def sum_dif(x):
    sum = 0
    for i in range(len(x)-1):
        sum += int(x[i+1]) - int(x[i])
    return sum

if __name__ == "__main__":
    fn = input("Enter the filename: ")
    inf = open(fn, "r")
    outf = open("lookea.3s.txt", "w")

    for word in inf:
        a = word[:-1]
        for i in range(1, len(word)-1):
            part1 = a[:i]
            sum1 = sum_dif(part1)
            part2 = a[i:]
            sum2 = sum_dif(part2)
            if sum1 == sum2:
                outf.write(part1+" "+part2+"\n")
                break

    inf.close()
    outf.close()
