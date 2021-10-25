import string 

#Try bloğu içinde kullanıcıdan alınan anahtar girdisi, 26 alfabetik harf içerip içermediğine göre incelenir.
# Farklı olasılıklar için oluşturulacak ValueError, ayrı mesajlara ayrılarak except tarafından yakalanır.

try:
    key = input("Key: ")
    if key.isalpha() and len(key) != 26:
        raise ValueError("Number of characters must be equal to 26.")
    elif not key.isalpha() and len(key) == 26:
        raise ValueError("Key must only contain alphabetical characters.")
    elif not key.isalpha() and len(key) != 26:
        raise ValueError("Key must contain 26 alphabetical characters.")
    else:
        pass
except ValueError as message:
    print(message)
    exit()

"""
#raise yerine assert kullanılarak istenen durumun doğruluğu sorgulanabilir.

try:
    key = input("Key: ")
    assert len(key) == 26 and key.isalpha()
except:
    print("Key must contain 26 alphabetical characters.")
    quit()
"""

key = key.upper() #key uppercase'e çevrilir

alphabet_list = list(string.ascii_uppercase) #uppercase alfabe karakterleri listelenir.

for char in alphabet_list:
    if key.count(char)!= 1: #count fonksiyonu kullanılarak alfabedeki karakterlerin key içindeki tekrarları incelenir.
        print("Key must contain different characters.")
        exit() #hatayla karşılaşılırsa program sonlarılır.        

"""
#alternatif 
# ord() yardımı ile key içinde rastlanan her harfin 0-26 aralığında değeri alınarak 26 elemandan oluşan buffer isimli listede kaydedilmesi sağlanır.
#Eğer karşılaşılan karakter bu liste içine daha önce eklenmişse, yani o indexte buffer[index] != 0 ise hata mesajı verilerek programdan çıkılır.

buffer = [0] * 26 #26 elemanlı buffer listesinin tüm indexlerde değeri 0'a eşitlenir

for i in range(26):
    if buffer[ord(key[i]) - 65] == 0: #karşılaşılan karakterin indexindeki değer 0 ise 1 arttırılır.
        buffer[ord(key[i]) - 65] += 1 
    
    else: 
        print("Key must contain different characters.") #karşılaşılan karakterin indexindeki değer 0 değilse key içinde aynı karakterin tekrarlandığı anlaşılır. 
        exit()
"""

plain_text = input("Plain text: ")

#şifrelenecek text için liste oluşturulur çünkü stringler değiştirilemezdir, kopyalanmış alfabetik olmayan karakterler şifrelenmez ve sonuca aynı şekilde yansır.
cipher_text = list(plain_text)

for i in range(len(plain_text)):
    
    #harfler dışındaki işaretler şifrelenmez ve büyük harf küçük harf uyumuna dikkat edilir.
    #plain_textte sıradaki harfin, alfabede kaçıncı sırada olduğu öğrenilirek key'de karşılık gelen harfle değiştirilir.
    
    if plain_text[i].isupper():
        cipher_text[i] = key[alphabet_list.index(plain_text[i])] 
    
    #eğer plain textte küçük harfle karşılaşılmışsa, bu karakterin alfabedeki indexini bulmak için plain_text[i].upper() kullanılarak büyük harf dönüşümü sağlanır.
    #Alfabeden index alındıktan sonra key'de karşılık gelen harf lower() ile küçültülerek cipher_text'e eklenir.
    
    if plain_text[i].islower():
        cipher_text[i] = key[alphabet_list.index(plain_text[i].upper())].lower() #ord metodu ve char aritmetiği -> key[ord(plain_text[i]) - 97].lower()

print("Cipher text:", "".join(cipher_text)) #join metodu ile cipher_text list veri tipinden string veri tipine çevrilir.
