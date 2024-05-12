while True:
    n = int(input("Hangi numaraya kadar yazılacağını girin: "))  #Girdi alıyoruz
    
    for i in range(1,n+1): #i'yi 1 den Kullanıcının girdiği sayıya kadar döner
        
        print((n-i)*"   ",end=" ")#Her satırın sol tarafına boşluk bırakarak desenin oluştururuz
        for j in range(i, 0,-1):#i' den başlayarak 0a kadar döner
            
            print(j, end="  ")#Her bir sayının arasına iki boşluk bırakır
        print()#Çıktıyı alırız
        
       
        
    
