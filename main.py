import pygame
import engine


# Global Variables
WIDTH = HEIGHT = 512
DIMENSIONS = 8
SQ_SIZE = WIDTH // DIMENSIONS
MAX_FPS = 15 # for animation latter
IMAGES = {}


def load_images():
    '''loads images from the pieces folder'''
    pieces = ['bb', 'bn', 'bq', 'bk', 'bp', 'wb', 'wn', 'wq', 'wk', 'wp'] # names of files to load
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("pieces/" + str(piece) + ".png"), (SQ_SIZE, SQ_SIZE))


def main():
    '''main driver. handles user input and updates the game state'''
    pass


if __name__ == "__main__":
    main()