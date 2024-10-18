ls=[("shirt",2,200),("pant",4,800),("phone",1,18000)]
print("--------------enter the details------------")
n=int(input("enter the no.of item you want to insert:"))
for i in range(0,n):
   a=str(input("enter name of item:"))
   b=int(input("enter name of quantity:"))
   c=int(input("enter name of price:"))
   x=(a,b,c)
   ls.append(x)
print(ls)
print("------------which element you want to remove---------")
o=str(input("enter name of item:"))
p=int(input("enter name of quantity:"))
q=int(input("enter name of price:"))
v=(o,p,q)
ls.remove(v)
key=lambda item:item[2]
print(sum(key))
