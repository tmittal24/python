#file handle, # read complete file
f = open("samplefile.txt", "r")
print(f.read())
f.close()

#Return the 5 first characters of the file:
f = open("samplefile.txt", "r")
print(f.read(6))
f.close()

#Read one line of the file:
f = open("samplefile.txt", "r")
print(f.readline())
f.close()

#Loop through the file line by line:
f = open("samplefile.txt", "r")
for x in f:
  print(x)
f.close()

# Note: You should always close your files, in some cases, due to buffering, changes made to a file may not show until you close the file.