fname = input("Enter file name: ")

#if nothing entered, use this file
if len(fname) < 1:
    fname = "mbox-short.txt"

try:
    fh = open(fname)
except:
    print("Entered wrong filename!")
    quit()

email = dict()

for line in fh:
    line = line.rstrip()
    if not line.startswith("From "): continue
    words = line.split()
    for word in words:
        print(words[1])
        #email[words[1]] = email.get(word,0) + 1


email_name = None
email_count =  None

for key, value in email.items():
    if email_count is None or value > email_count:
        email_name = key
        email_count = value

print(email_name, email_count)