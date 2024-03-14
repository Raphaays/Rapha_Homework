meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "YTTA" : "YTTA, Atau Yang Tau Tau aja",
            "Fyp" : "Fyp adalah singkatan dari For You Page",
            "Fyi" : "Fyi adalah singkatan dari For Your Information",
            "STFU" : "curse word untuk menyuruh orang diam",
            "Pookie" : "panggilan sayang untuk teman (biasanya di gunakan oleh perempuan.),
            }
            
word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")

print (meme_dict.keys())

if word in meme_dict.keys():
   print (meme_dict[word])
else:
   print('Sorry That Word Not Avaible')
