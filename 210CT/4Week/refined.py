def p(g):
 for i in z(l(g)//2):
  if g[i]!=g[l(g)-i-1]:return False
 return True
t=input();m="";s=[];l=len;z=range
for i in z(l(t)):
 for j in z(i+1,l(t)):s.append(t[i:j+1])
for e in s:
 if p(e):
  if l(e)>l(m):m=e
print(m)