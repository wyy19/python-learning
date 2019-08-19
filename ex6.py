#replace %d with 10
x = "There are %d types of people." % 10
#assign string "binary" to variable binary
binary = "binary"
#assign string "don't" to variable do_not
do_not = "don't"
#replace the first %s with the value of variable binary and replace the second %s with the value of variable do_not
#assign the string to variable y
y= "Those who know %s and those who %s." %(binary,do_not)

#print out the value of variable x
print(x)

#print out the value of variable y
print(y)


print("I said: %r." % x)
print("I also said: '%s'." %y)


hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation %hilarious)



w = "This is the left side of ..."
e = "a string with a right side."

print(w + e)


