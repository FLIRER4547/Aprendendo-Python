
import pygame


a=input('cole o diretório da música aqui:')
pygame.mixer.init()
pygame.mixer.music.load(a)
pygame.mixer.music.play(loops=-1)
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

