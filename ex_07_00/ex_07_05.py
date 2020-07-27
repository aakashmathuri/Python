fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1:
        continue
    # find() method is used for find  from the given characters.
    print(line)
