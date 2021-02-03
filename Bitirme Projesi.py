import time
while True: 
    dosya = open("C:\\Users\\hatic\\Desktop\\tarama.txt", "r") 
    aranan = input("Belgede aramak istediğiniz İp adresini giriniz: ")
    aranan_varmi = dosya.read().find(aranan) 
    
    if aranan_varmi != -1:
        time.sleep(2)
        secenek = str (input("İp adresi bulundu. Engellemek ister misiniz?:(y/n):"))
        if secenek == 'y':
            time.sleep(2)
            print("Engellenmiştir.") 
            time.sleep(10)    
            break  
        tercih = str (input("Tekrar İp aramak ister misiniz?:(e/h):"))  

        if tercih == 'h':
            print("Tekrar Görüşmek üzere")
            dosya.close() 
            time.sleep(10)
            break

    if aranan_varmi == -1:
        time.sleep(2)
        print("Aradığınız İp adresi bulunamamıştır tekrar deneyiniz.")
        time.sleep(10)
        break
	
    
    
    
    
    
    
   

    
