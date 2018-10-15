def s(a):
 r=[[1 for x in range(5)] for y in range(5)];e=[] 
 for x in range(len(a)):
  for y in range(len(a)):    
   if (x,y) in e:
    continue               
   if a[x][y]=="H":
    r[x][y]="H"        
   elif a[x][y]=="I":
    r[x][y]="F"         
    for m in range(-1,2):
     for k in range(-1,2):
      if m!=k and m!=-k: 
       try: 
        if a[x+m][y+k]=="H":
         r[x+m][y+k]="I";e.append((x+m,y+k))
       except:
        pass
   elif a[x][y]=="F":
    r[x][y]="H" 
 return r
a=[[1 for x in range(5)] for y in range(5)];j=0
for l in open("i","r").readlines():  
 i=0 
 for e in l:
  if e!=" ":
   if i==5:
    break
   a[j][i]=e;i+=1 
 j+=1 
g=int(input())
for i in range(g):
 a=s(a)
for i in range(len(a)):
 for j in range(len(a)):
  print(a[i][j],end=" ")
 print("")