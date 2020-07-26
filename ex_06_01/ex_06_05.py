text = "X-DSPAM-Confidence:    0.8475"
ipos = text.find(':')
#print(ipos)
slice = text[ipos+5:]
#print(slice)
val = float(slice)
print(val)
