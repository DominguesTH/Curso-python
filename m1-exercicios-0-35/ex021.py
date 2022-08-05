# DESAFIO: Faça um programa em python que abra e reproduza o áudio de um arquivo mp3.

import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('m1-exercicios-0-35\ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
