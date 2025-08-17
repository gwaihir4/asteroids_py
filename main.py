import pygame
import sys
from constants import *
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0

    group_updatable = pygame.sprite.Group()
    group_drawable = pygame.sprite.Group()
    group_asteroids = pygame.sprite.Group()
    group_shots = pygame.sprite.Group()

    Player.containers = (group_updatable, group_drawable)
    Asteroid.containers = (group_asteroids, group_updatable, group_drawable)
    AsteroidField.containers =(group_updatable)
    Shot.containers = (group_shots, group_updatable,group_drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))    
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    astro_field = AsteroidField()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        group_updatable.update(dt)
        for asteroid in group_asteroids:
            if player1.collides_with(asteroid):
                print("Game over!")
                sys.exit()
            for shot in group_shots:
                if shot.collides_with(asteroid):
                    shot.kill()
                    asteroid.split()
        for entity in group_drawable:
            entity.draw(screen)
        pygame.display.flip()
        dt = game_clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()
