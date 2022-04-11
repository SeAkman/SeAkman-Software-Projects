import random
girilenharfler=[]
isimtam=[]
isim1=["a","h","m","e","t"]
isim1tam=["ahmet"]
isim2=["m","e","h","m","e","t"]
isim2tam=["mehmet"]
isim3=["k","e","m","a","l"]
isim3tam=["kemal"]
isim=[isim1,isim2,isim3]
secim1=random.choice(isim)
secim2=random.choice(isim)
if secim1 == isim1:
    isimtam=isim1tam
elif secim1 == isim2:
    isimtam=isim2tam
elif secim1 == isim3:
    isimtam = isim3tam

cizgi=(len(secim1))
tcizgi=cizgi*["_ "]
print(tcizgi)
k=0
i=0
while k<8:
    if not "_ " in list(tcizgi):
        print("oyun bitti oyunu kazandın")
        break
    elif k==7 and "_ " in list(tcizgi):
        print("oyun bitti oyunu kaybettin")
        break    
    th=str(input("tahminde bulun ya da harf söyle(t/h)"))

    if th == "h":            
        harf=str(input("harf girin"))
        i=0
        while i<len(secim1):
            if str(harf) in (list(secim1)):
                if secim1[i] == harf:
                    if tcizgi[i] != "_ ":
                        print("bu harfi zaren daha önce kullandınız")
                        break
                    tcizgi.pop(i)
                    tcizgi.insert(int(i),str(harf))
                    print("doğru harf")
                    print(tcizgi)
                    i=i+1
                else:
                    i=i+1 
            else:
                print("harf yanlş bilindi")
                k=k+1
                break            
    elif th == "t":
        tahmin=str(input("Tahmininiz Nedir"))
        if str(tahmin) in (str(isimtam)):
            print("tebrikler kelimeyi doğru bildiniz: "+str(secim1))
            break
        
        else:
            print("kelime yanlış")
            k=k+1
        


        

        
    
    
