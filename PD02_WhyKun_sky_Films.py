#1uzd.
filma = {
    'nosaukums' : 'Peaky Blinders',
    'režisors' : 'Oto Batērsts un Toms Hārpers',
    'žanrs' : 'drama',
    'aktieri' : ['Киллиан Мерфи', 'Хелен Маккрори ...']
}

print(filma)

filma['IMBD_reitings'] = 9.4

#maina žanru
filma['žanrs'] = 'trilleris,kriminals'
#izdzes režisoru
del filma['režisors']
filma2= {
    'nosaukums': 'Castelvania',
    'žanrs' : 'Vampiri, Anime',
    'aktieri' : ['Alucard, Dracula, ... '],
    'IMDB_reitings' : 9.5
}

filmas={'filma1' : filma, 'filma2' : filma2}

#izdruka vardnicu

print(filma)
print(filma2)