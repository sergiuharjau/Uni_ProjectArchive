def s(a):
 r=[1]*25;e=[]
 for i in z(25):
  if i in e:k=0
  elif a[i]=="I":
   r[i]="F"
   for x in [-5,-1,1,5]:
    try:
     if i%5 in (0,4) and x in (-1,1):k=0
     elif a[x+i]=="H":r[x+i]="I";e.append(x+i)
    except:k=0
  else:r[i]="H"
 return r
z=range;a=[]
a=open("i","r").read().replace('\n','')
for i in z(int(input())):a=s(a)
for i in z(25):
 print(a[i],end="")
 if (i+1)%5==0:print()