fhand = open('mbox-short.txt')

for line in fhand:
    line = line.rstrip()        # rstrip() method remove all whitespace.
    if line.startswith('From:'): # startswith() method is used for whatever word or characters we want to print from.
        print(line)
