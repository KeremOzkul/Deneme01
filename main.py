meme_dict = {
    "CRINGE": "Garip ya da utandırıcı bir şey",
    "LOL": "Komik bir şeye verilen cevap",
    "RANDOM": "Bir Cümleye Gülme Anlamında Spamlanan(Spam Kelimesini Bilmiyorsanız Sözlükte Mevcut) Rastgele Harfler",
    "SPAM": "Bir Mesaj Veya Yazının Durmadan Yazılması Veya Tekrarlanması",
    "SHEESH": "onaylamamak",
    "CREEPY": "korkunç",
    "AGGRO": "agresifleşmek/sinirlenmek",
    "ROFL": "bir şakaya karşılık cevap",
}

while True:
    word = input("Merhabalar! Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    
    if word in meme_dict:
        print(meme_dict[word])
        break
    else:
        print("Malesef Dediğiniz Kelime Henüz Kütüphanemizde Yok Veya Yanlış Yazdınız. Tekrar Deneyin.")
