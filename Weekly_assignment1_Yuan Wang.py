
Width=float(input("How much is the width of your room?(in meter)It is :"))
Length=float(input("How much is the length of your room?(in meter)It is :"))
Height=float(input("How much is the Height of your room?(in meter)It is :"))

Volume=Width*Length*Height
Area=Width*Length
print("hello,your room is " + str(Area) + " square meters")
print("hello,your room is " + str(Volume) + " cubic meters")

mmVolume=Volume*1000000000
mmArea=Area*1000000
print("hello,your room is " + str(mmArea) + " square milimeters")
print("hello,your room is " + str(mmVolume) + " cubic milimeters")

if Width>Length:
   if Width>Height:
     print("The Width of your room surpasses both its Length and Height,it is "+str(Width))
   else:
      print("The Height of your room surpasses both its Width and length,it is "+str(Height))
elif Width < Length:
   if Height > Length:
      print("The Height of your room surpasses both its Width and length,it is "+str(Height))
   else:
      print("The Length of your room surpasses both its Width and Height,it is "+str(Length))
else:
   if Height > Width:
      print("The Height of your room surpasses both its Width and Height,it is "+str(Height))
   elif Height < Width:
      print("The Width and Length of your room surpasses its Height ,it is "+str(Width))
   else:
      print("all the dimensions are the same,it is "+str(Width))
      