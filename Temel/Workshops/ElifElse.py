# -*- coding: utf-8 -*-

lights = ["red","yellow","pink"]

currentlight = lights[2]

print(currentlight)

if currentlight == "red":
    print("stop")
elif currentlight == "yellow":
    print(" be ready")    
else currentlight == "green": #( burayı yazmayız direk else :)
    # bu durumlarda verilen değeri basar ama else yaparsak sonuncuyu basar
    print("go")
