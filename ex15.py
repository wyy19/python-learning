#from sys import argv

#script, filename = argv

#txt = open(filename)

#print("Here's your file %r:" % filename)
#print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print("print based on line ------>")
print(txt_again.readline())
print("print based on lines ------>")
print(txt_again.readlines())
print("print the entire content ------>")
print(txt_again.read())
txt_again.close()


