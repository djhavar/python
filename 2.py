t1=('1','2','3','4','5')
print(t1)
t2=('a','b','c','d','e','f','g','h','i')
print(t2)
t3=('false','true','false','true','false','true','false','true')
print(t3)

print(len(t1))
print(len(t2)) 
print(len(t3)) 


t4 = t1 + t2 + t3
print(t4)
print(len(t4)) 

print(t4[5])
print(t4[6])
print(t4[7])
print(t4[8])

print(t4[5:11])
print(t4[:11])
print(t4[5:])

t1=('1','2','3','4','5')
if "4" in t1:
print("yes, '4' is in t1")