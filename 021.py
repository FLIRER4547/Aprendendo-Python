
import pygame
a=input('cole o diretório da música aqui: ').strip().strip("").strip('"')
pygame.mixer.init()
pygame.mixer.music.load(a)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
<<<<<<< HEAD

=======
>>>>>>> 0af5b84 (adicionar todos os arquivos)
