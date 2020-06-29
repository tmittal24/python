# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

# 1 - Write to an Existing File
f = open("samplefile.txt", "a")
f.write("Now the file has more content! after append")
f.close()
#open and read the file after the appending:
f = open("samplefile.txt", "r")
print(f.read())
f.close()


# 2- Open the file "demofile3.txt" and overwrite the content:
f = open("samplefile.txt", "w")
f.write("Woops! I have deleted the existing content! by this line")
f.close()
#open and read the file after the appending:
f = open("samplefile.txt", "r")
print(f.read())