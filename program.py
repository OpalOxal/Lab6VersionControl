#It takes a name input
#It takes some other string
#It adds the string between every letter of the name
name = input("Input name: ")
other = input("Input something to add after every letter: ")
longerName = ""
for i in range(len(name)):
    longerName = longerName + name[i] + other
print(longerName)
