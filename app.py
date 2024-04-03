import sys
import pygame

import numpy as np
from random import randint
from perlin_numpy import (
    generate_perlin_noise_2d
)

pygame.init()

class Main:
    
    global block_image
    
    clock = pygame.time.Clock()
    
    screen = pygame.display.set_mode((600, 600), 0, 32)
    display = pygame.Surface((300, 300))
    
    block_image = pygame.image.load('block.png')
    
    seed = randint(0, 5000)
    np.random.seed(seed)
    print("Seed :", seed)
    noise = generate_perlin_noise_2d((15, 15), (1, 1))
    
    def text_to_map_data(path):
        map_file = open(path)
        # Mettre chaque ligne du fichier texte dans une matrice
        map_data = [[int(c) for c in row] for row in map_file.read().split('\n')]
        map_file.close()
        return map_data
    
    def noise_to_text(surface, noise):
        for i in range(len(noise)):
            for j in range(i):
                noise[i][j] = noise[i][j] * 10
                
        noise = np.trunc(noise)

        for y, row in enumerate(noise): # enumerer chaque listes de la matrice
            for x, tile in enumerate(row): # enumerer chaque elements de chaque listes
                surface.blit(block_image, (140 + x * 10 - y * 10, 100 + x * 5 + y * 5 - tile * 10))

        print(noise)
    
    def text_to_render_map(surface, data, layer=0, debugView=False):
        for y, row in enumerate(data): # enumerer chaque listes de la matrice
            for x, tile in enumerate(row): # enumerer chaque elements de chaque listes
                if tile and debugView: # Si il y a un 1 dans la liste et que le debugView est active
                    # On affiche des rectangles blancs
                    pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
                elif tile: # Si il y a seulement un 1 dans la liste
                    # On affiche l'image du bloc avec ses coordonnees pour l'effet isometrique
                    surface.blit(block_image, (140 + x * 10 - y * 10, 100 + x * 5 + y * 5 - layer * 10))
    
    dataLayer0 = text_to_map_data('mapLayer0.txt')
    dataLayer1 = text_to_map_data('mapLayer1.txt')
    dataLayer2 = text_to_map_data('mapLayer2.txt')
    
    #noise_to_text(display, noise)
    text_to_render_map(display, dataLayer0, 0)
    text_to_render_map(display, dataLayer1, 1)
    text_to_render_map(display, dataLayer2, 2)
    
    while True:
        
        screen.fill((0, 0, 0))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                
        screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
        pygame.display.flip()
        clock.tick(60)
        
if __name__ == '__main__':
    Main()