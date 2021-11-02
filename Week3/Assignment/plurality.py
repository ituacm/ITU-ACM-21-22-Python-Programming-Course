#global değişken, bu sözlük adayların oy sayımlarını tutmak için oluşturulmuştur.
candidateDict = {}

def vote():
    #Seçmen adaylardan herhangi birine oy vermiyorsa tekrar seçim yapması istenir.
    #doğru giriş yaptıysa seçtiği adayın oy sayımı 1 arttırılır
    candidate_name = input("Vote: ")
    
    if candidate_name == "Q" or candidate_name == "q":
        return False
        
    while candidate_name not in candidateDict:
        print("Invalid vote.")
        candidate_name = input("Vote: ")
    
    candidateDict[candidate_name] += 1
    return True

#kazananın yazdırılması için oluşturulmuş bu fonksiyonda,
#oy sayılarında eşitlik olması durumunda birden çok galip oluşabilir.
def print_winner():

    highest_vote = max(candidateDict.values()) #en yüksek oylanma değeri alınır.

    print("Winner(s): ")

    for candidate in candidateDict.items(): #en yüksek oya sahip aday ya da adaylar(kazananlar) yazdırılır.
        if candidate[1] == highest_vote:
            print(candidate[0])
    return
    

#adayları içeren bir set oluşturulur ve isimlerinde alfabetik olup olmadığı kontrol edilerek sözlüğe ekleme yapılır.
candidateSet = set((x.capitalize() for x in input("Please enter the names of the candidates seperated by commas: ").split(', ')))

for name in candidateSet:
    if name.isalpha():
        candidateDict[name] = 0 #set içindeki alfabetik isimler sözlüğün anahtarlarını oluşturur ve başlangıç değeri olarak 0 alırlar.

del candidateSet #seti sil 

#her iterasyonda vote() fonksiyonu çağrılarak kullanıcıdan Q ya da q girene kadar oylama yapması istenir.
while(vote()):
    pass

print_winner()
