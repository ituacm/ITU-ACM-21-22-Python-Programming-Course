# istenen input 16, 15, ya da 13 basamklı bir kart numarası olmalıdır, 
# bunu sağlamak için do-while yapısına benzer bir loop kullanılır.

number = input("Card number: ")

while number.isnumeric() == False:
    number = input("Card number: ") #number string formunda olduğundan len() foksiyonu kullanılabilir.

count = len(number) #sayının kaç basamaklı oldupu hesaplanır.
first_two = int(number[count - 2 : count]) #sayının son iki rakamı alınır - alternatif : last_two = number // 10 ** (count -2)
number = int(number)
sum = 0


while number:

    #Tek basamaktaki rakam sum'a eklenir.
    # Sonrasında sum 10'a bölünerek sıradaki rakama geçilir.
    sum += number % 10 
    number //= 10
    
    #burada çift basamaktaki rakam ikiyle çarpılarak rakamları toplanır. 
    # General approach yerine for loop da tercih edilebilir.
    sum += ((number % 10) * 2) % 10 + ((number % 10) * 2) // 10 
    
    #sum güncellendikten sonra sayı tekrar 10'a bölünür. 
    # Burada amaç sonraki iterationda tek basamaktaki rakama geçmektir.
    number //= 10

#sum'ın son rakamı 0 değil ise kart geçerli değildir. 
# Bu koşul sağlanırsa iç içe geçmiş if else satırları ile kart tipi olasılıkları kontrol edilir. 
# Uyum sağlanmazsa "invalid" yazdırılır.

if sum % 10 == 0:

    if count == 15 and (first_two == 34 or first_two == 37):
        print("AMEX")
    
    elif count == 16 and (first_two >= 51 and first_two <=55):
            print("MASTERCARD")
    
    elif (count == 16 or count == 13) and first_two // 10 == 4:
            print("VISA")

    # Uyum sağlanmazsa "invalid" yazdırılır.
    
    else:
        print("INVALID")

else:
    print("INVALID")
