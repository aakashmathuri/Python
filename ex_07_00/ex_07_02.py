fhand = open('mbox-short.txt')
inp = fhand.read()  #read() is a method for reading the file from secondary memory.
print(len(inp))     #len() is for finding length of a file.
print(inp[:20])     #[:20] means all characters start from and upto 20 index
