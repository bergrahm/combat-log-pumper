import pygame
import time
pygame.init()
song = pygame.mixer.Sound('SFX/mMurlocAggroOld.ogg')
#clock = pygame.time.Clock()
song.play()
time.sleep(0.5)
BL = pygame.mixer.Sound('SFX/Bloodlust_player_cast_head.ogg')
#clock = pygame.time.Clock()
BL.play()
time.sleep(3)
pygame.quit()
