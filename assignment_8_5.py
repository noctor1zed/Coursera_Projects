fname = input("Enter file name: ")

#if nothing entered, use this file
if len(fname) < 1:
    fname = "mbox-short.txt"

try:
    fh = open(fname)
except:
    print("Entered wrong filename!")
    quit()

count = 0
email = list()

for line in fh:
    line = line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()
    email.append(words[1])
    print(email[count])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")