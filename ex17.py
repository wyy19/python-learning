from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Coping from %s to %s" %(from_file, to_file))

indata = open(from_file).read()

print("""
The input file is %d bytes long,
Does the output file exist?%r,
Ready, hit RETURN to continue, CTRL-C to abort.
""" % (len(indata), exists(to_file)))
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
