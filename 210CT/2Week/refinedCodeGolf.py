def s(a):
 r=[[1]*5 for y in z(5)];e=[] 
 for x in z(5):
  for y in z(5):    
   if (x,y) in e:j=0                     
   elif a[x][y]=="I":
    r[x][y]="F"
    for m in z(-1,2):
     for k in z(-1,2):
      if m!=k and m!=-k: 
       try:
        if a[x+m][y+k]=="H":r[x+m][y+k]="I";e.append((x+m,y+k))
       except:j=0
   else:r[x][y]="H"
 return r
z=range;a=[[1]*5 for y in z(5)]
for j in z(5):
 for i in z(5):a[j][i]=open("i","r").readlines()[j][i]
for i in z(int(input())):a=s(a)
for x in z(5):
 for y in z(5):print(a[x][y],end="")
 print()