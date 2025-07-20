#supermarket bill generation
name=input("enter customer name:")
#list of items
list='''  
Rice           Rs 50/kg
Sugar          Rs 30/kg
Oil            Rs 120/liter
Maggie         Rs 12/pack
Paneer         Rs 40/kg
Horlicks       Rs 250/bottle
'''
#declaration
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

items={'Rice':50,'Sugar':30,'Oil':120,'Maggie':12,'Paneer':40,'Horlicks':250}
while True:
    option=input("press 1 for list or 2 to exit: ")
    if option=='2':
        print("thank you  for shopping")
        break
    elif option=='1':
        print(list)
        while True:
            inp1=input("press 1 for shopping or 2 to exit:")
            if inp1=='2':
                print("Thank you for shopping")
                break
            elif inp1=='1':
                item=input("enter the items:")
                quantity=int(input("enter the quantity:"))
            if item in items:
                price=quantity*(items[item])
                pricelist.append((item,quantity,price))
                totalprice+=price
                ilist.append(item)
                qlist.append(quantity)
                plist.append(price)
                tax=(totalprice*10)/100
                finalprice=tax+totalprice
            else:
                print("item is invalid")
        else:
            print("entered number is invalid")
        inp=input("bill the items yes or no:")
        if inp=='yes':
           pass
           if finalprice!=0:
              print("-"*60,"Super supermarket","-"*60)
              print("Name:",name)
              print("-"*123)   
              print("sno"," "*30,"items"," "*30,"quantity"," "*30,"price")
              for i in range(len(pricelist)):
                print(i," "*30,ilist[i]," "*30,qlist[i]," "*30,plist[i])
              print("-"*143)
              print(" "*60,"totalamount:","Rs",totalprice)
              print("taxamount"," "*53,"tax:Rs",tax)
              print("-"*60)
              print(" "*60,"finalamount:","Rs",finalprice)
              print("-"*143)
              print(" "*60,"THANKS FOR VISITING")
              print("-"*143)
        break        
                
                
            
        
    
     


                        






