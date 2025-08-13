def count_letters(word):
    letter_count = {} #kelimelerin sayısını tutan sözlük
    for char in word: # "word" olarak verilen her kelimedeki "char" için
        if char in letter_count: # eğer ki "char" sözlükte zaten varsa:
            letter_count[char] += 1 # sayısını 1 arttır
        else: # yoksa
            letter_count[char] = 1 # ilk kez ekle
        #letter_count[char] = letter_count.get(char, 0) + 1  # Bu da üstteki 3 satırın özeti
    return letter_count # sözlüğü döndür

def find_anagrams(word, candidates):
    word_lower = word.lower() #aranacak kelimeyi küçük harfe çevir
    word_letter_count = count_letters(word_lower) # aranacak kelimenin harflerini çevir ve al
    
    result = [] # boş bir sonuç değişkeni, sonradan içine ekleyeceğiz

    for candidate in candidates: # aday kelimelerimizin tamamındaki her bir "candidate" için
        cand_lower = candidate.lower() # bu kelimeyi küçük harfe çevir

        if cand_lower == word_lower: # Eğer kelime aranan kelimeyle birebir aynıysa olmaz
            continue  # kendisiyle eşleşme koda devam et

        if count_letters(cand_lower) == word_letter_count: # eğer kelime aradığımız şartlara uyuyorsa
            result.append(candidate)  # orijinal haliyle ekle, çünkü exercism böyle bekliyor. İyi çalışmalar.

    return result
