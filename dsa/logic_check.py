st="abcde"
df=list(st)
mm=[i+j+k+l+m for i in df for j in df for k in df for l in df for m in df]
mm1=set([jk[2:] for jk in mm])
mm2=set(mm1)
print(mm2)
