file = open("samplefile.txt", "r")
total_count = 0
for line in file:
    #line = (file.readline())
    print(line)
    for word in line.split():
        if str(word) == "and":
            lineCount = line.count(word)
            total_count = total_count + lineCount
            print(word + " -> comes " + str(lineCount) + " times in this line.")
    print("total count = " + str(total_count))
