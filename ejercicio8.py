Precio = input("Enter de price:" )

print("Euros: ", Precio[:Precio.find(".")], "centimos: ", Precio[Precio.find(".")+1:])
