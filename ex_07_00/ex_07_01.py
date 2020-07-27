count = 0
fopn = open('mbox-short.txt')   #open is a methon for Open a file form secondary memory.
for line in fopn:
    count = count + 1
print('Line count:',count)
