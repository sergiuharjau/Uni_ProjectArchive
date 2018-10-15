z=range;o=len;p=print
def s(a):
 r=[[1]*5 for y in z(5)];e=[] 
 for x in z(o(a)):
  for y in z(o(a)):    
   if (x,y) in e:continue               
   if a[x][y]=="H":r[x][y]="H"        
   if a[x][y]=="I":
    r[x][y]="F"         
    for m in z(-1,2):
     for k in z(-1,2):
      if m!=k and m!=-k: 
       try:
        if a[x+m][y+k]=="H":r[x+m][y+k]="I";e.append((x+m,y+k))
       except:pass
   if a[x][y]=="F":r[x][y]="H" 
 return r
a=[[1]*5 for y in z(5)]
for j in z(5):
 for i in z(5):a[j][i]=open("i","r").readlines()[j][i]
g=int(input())
for i in z(g):a=s(a)
for i in z(o(a)):
 for j in z(o(a)):p(a[i][j],end="")
 p()