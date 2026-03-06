userRegistered= True
shoppingCart= 0
if userRegistered == True and shoppingCart >=1:
    print("You can proceed to payment!")

elif userRegistered == 'guest' and shoppingCart==0:
    print("You can proceed to payment!")

else:
    print("You can't proceed to payment!")