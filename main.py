meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "CREEPY": "menakutkan, tidak menyenangkan",
            "KODOKACUMALAKA": "kodok ngakak sampoe salto",
            "SKIBIDI": "makhluk yang berbadam toilet dan sangat sigma",
            "ambatukam": "pake huruf kapital kocak",
            "AMBATUKAM": "makhluk misterius yang berasal dari ngawi empire temannya mas ironi dan memiliki level sigma 3jt"          
            }

word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

if word in meme_dict.keys():
    print("Makna kata",word,"adalah",meme_dict[word])
else:
    print('kata tidak ditemukan')
