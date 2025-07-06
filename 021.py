<<<<<<< HEAD
import pygame


a=input('cole o diretório da música aqui:')
pygame.mixer.init()
pygame.mixer.music.load(a)
pygame.mixer.music.play(loops=-1)
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)





=======
import pygame


a=input('cole o diretório da música aqui:')
pygame.mixer.init()
pygame.mixer.music.load(a)
pygame.mixer.music.play(loops=-1)
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)





>>>>>>> 906f683d003e5866a5a93655b2e63bfb4323763d
