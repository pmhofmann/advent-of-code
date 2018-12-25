inputfile = open('AdventDay1Input', 'r')
frequencies = inputfile.read().splitlines()
inputfile.close()
results = map(int, frequencies)

testlist = [1, 2, 3, -9, 5]
testlist1 = [1, -1]
testlist2 = [3, 3, 4, -2, -4]
testlist3 = [-6, 3, 8, 5, -6]
testlist4 = [7, 7, -2, -7, -4]
#results = testlist2
sum = 0
sums_seen = [0]
duplicateFound = False
while duplicateFound == False:
    for element in results:
        sum = sum + element
        print sum
        if sum in sums_seen:
            duplicateFound = True
            print sum
            break
        sums_seen.append(sum)
