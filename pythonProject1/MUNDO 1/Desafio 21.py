# Faça um programa que reproduza um áudio em MP3

import pygame

pygame.init()
pygame.mixer.music.load('ex.21.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()