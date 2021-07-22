from playsound import playsound
from os import chdir, getcwd, listdir
from random import randrange

cam = input('Informe o caminho: ')

chdir(cam)
print(getcwd())

for letra in cam:
    if letra == '\\':
        cam = cam.replace('\\', '/')

musicas = []
for indice, c in enumerate(listdir()):
    print([indice], c)
    musicas.append(c)
else:
    print([indice + 1], 'Aleatória')

musica = int(input('Informe o indice da música que você quer: '))

if musica >= int(len(musicas)):
    aleatorio = randrange(len(musicas))
    aleatorio = musicas[aleatorio]
    musica = aleatorio
else:
    musica = musicas[musica]

playsound(f'{cam + "/" + musica}')
