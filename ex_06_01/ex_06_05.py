text = "X-DSPAM-Confidence:    0.8475"
ipos = text.find(':')
print(ipos)
slc = text[ipos + 5:]
print(slc)
vL = float(slc)
print(vL)
