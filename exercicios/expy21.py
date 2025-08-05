# reprodução de um áudio mp3
import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('expy21.mp3')
pygame.mixer.music.play()
pygame.event.wait()