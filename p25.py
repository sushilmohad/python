s= [10,15,12,45,16,74,22,2,18]
a=len(s)
maxpos = s.index(max(s))
minpos = s.index(min(s))
s[minpos]=s[maxpos]+1
print(s)
