f = open("test.txt")
filelines = f.readlines()
for line in filelines:
    print(line)

introstring = "my name is narayan, i am in 10th grade"
word = introstring.split(",")
print (word)

def greet(name):
    print ("hello"+name)
greet ("narayan")    