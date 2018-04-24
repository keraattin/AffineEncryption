
#alphabet = ['a','b','c','ç','d','e','f','g','ğ','h','ı','i','j','k','l','m','n','o','ö','p','r','s','ş','t','u','ü','v','y','z']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

#Deşifreleme fonksiyonu
def decryption(cipher,a,b):
    ptArray = list(cipher)  #String'in her karakteri ayrılıp liste olusuturluyor.

    #z değeri bulunuyor
    z = 0
    for i in range(1,29):
        if ((int(a)*int(i)) % int(len(alphabet)) ) == 1:
            z = i

    valArray = []
    decryptedArray = []

    #Her stringe karşılık gelen alfabedeki sayı değeri valArray'e alınıyor.
    for i in ptArray:
        for k,val in enumerate(alphabet):
            if i == val:
                valArray.append(k)

    #valArray'deki değerler z(y-b) mod 29 ile işleme sokulup çözülüyor ve karakter karşılığı decryptedArray dizisine yazılıyor.
    for i in valArray:
        y = (int(z) * (int(i)-int(b)) ) % int(len(alphabet))
        decryptedArray.append(alphabet[y])

    decryptedString = ""

    #Dizinin her elemanı birleştirilerek çözülmüş metin ortaya çıkarılıyor.
    for i in decryptedArray:
        decryptedString += i

    print("Anahtar degeri : (",a,",",b,")")
    print("Çözülmüş metin : ",decryptedString)

#Şifreleme fonksiyonu
def encryption(plainText,a,b):
    ptArray = list(plainText)   #String'in her karakteri ayrılıp liste olusuturluyor.

    valArray = []
    encryptedArray = []

    #Her stringe karşılık gelen alfabedeki sayı değeri valArray'e alınıyor.
    for i in ptArray:
        for k,val in enumerate(alphabet):
            if i == val:
                valArray.append(k)

    #valArray deki her değer ax+b mod 29 ile işleme sokulup karakter karşılığı encryptedArray dizisine yazılıyor.
    for i in valArray:
            y = ((int(a) * + int(i)) + int(b) ) % int(len(alphabet))
            encryptedArray.append(alphabet[y])

    encryptedString = ""

    #Dizinin her elemanı birleştirilerek şifrelenmiş string oluşturuluyor.
    for i in encryptedArray:
        encryptedString += i

    print("Şifrelenmiş metin : " ,encryptedString)
    return encryptedString

#Aralarında asal olup olmadıklarını belirleyen fonksiyon
def isPrimeBetween(x,y):
    edge = 0
    if x > y:
        edge = x
    else:
        edge = y

    for i in range(2,edge):
        if int(x) % int(i) == 0 and int(y) % int(i) == 0:
            return False

    return True


message = input("Şifrelenecek metini giriniz : ")   #Kullanıcıdan mesaj alınıyor.
a = input("a degerini giriniz : ")                  #Anahtarın a değeri alınıyıor.
b = input("b degerini giriniz : ")                  #Anahtarın b değeri alınıyor.

message = message.lower()   #Büyük harf ile bir mesaj girilmiş ise onu küçük harfe çeviriyor.

print(len(alphabet))

#Girilen mesajın içinde sayı olup olmadığu kontrol ediliyor.
for i in message:
    if i.isnumeric() == True:
        print("Lütfen bir string mesaj giriniz")
        exit(0)

#Girilen a değerinin sayı olup olmadığı kontrol ediliyor.
if a.isnumeric() == False:
    print("a degeri bir sayı olmalıdır")
    exit(0)

#Girilen b değerinin sayı olup olmadığı kontrol ediliyor.
if b.isnumeric() == False:
    print("b degeri bir sayı olmalıdır")
    exit(0)

#Girilen a ve b değerlerinin 0 dan büyük ve alfabeden küçük olması kontrol ediliyor.
if int(a)>len(alphabet) or int(a)<1 or int(b)>len(alphabet) or int(b)<1:
    print("Lütfen 1 ile ",len(alphabet)," arasında anahtar değeri giriniz")
    exit(0)

#Girilen a ile n değerinin aralarında asal olup olmadığı kontrol ediliyor.
if  isPrimeBetween(int(a),len(alphabet)) == False:
    print("a ile n değeri aralarında asal olmalıdır.")
    exit(0)

encryptedString = encryption(message,a,b)  #Şifrelenmiş mesaj elde ediliyor.

counter = 0 #Kaç deneme yapıldığını gösteren sayaç.

#Tüm olası anahtar degerleri deneniyor.
for a in range(1,len(alphabet)):
    if isPrimeBetween(int(a), len(alphabet)) == True:
        for b in range(1,len(alphabet)):
                decryption(encryptedString, a, b)
                counter += 1

print(counter)
