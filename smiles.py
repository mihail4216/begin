

f= open('text.txt','r')
smile_list=list()
for i in f:
    i=i.strip()
    i=i.replace('+','000')
    smile_list.append(i)
f.close()
print smile_list
