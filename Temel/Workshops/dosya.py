

f = open("musteri.txt" )
#print(f.read())   tamamını okur
print("******")

for I in f:
    print(I)


#print(f.readline()) satır satır okuma işlemi yapar.
# r = read ,  a = append , w = write , x = create

f.close()

fileToAppend = open("ogrenciler.txt", "w")  # w komutu siler ve üstüne yazar 
fileToAppend.write("\n")
fileToAppend.write("ahmet")
#%%


    

import os


#os.remove ("ogrenciler.txt)   dosyayı siler

if os.path.exists("ogrenciler.txt"):
    os.remove("ogrenciler.txt")
    
else  :
  print("dosya yok")   
  
  
 os.rmdir("ogrenciler.txt") 
    