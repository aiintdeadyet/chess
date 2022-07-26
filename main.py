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
    # only done once before the while loop
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color('white'))
    game_state = engine.game()
    load_images() 
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # get the mouse position
                pos = pygame.mouse.get_pos()
                # get the square that the mouse is on
                row, col = pos[1] // SQ_SIZE, pos[0] // SQ_SIZE
                # get the piece that is on that square
                piece = game_state.board[row][col]
                # if the piece is a white piece and it is the player's turn, move the piece
                if piece.isupper() and game_state.turn == 'white':
                    game_state.move(row, col)
                # if the piece is a black piece and it is the player's turn, move the piece
                elif piece.islower() and game_state.turn == 'black':
                    game_state.move(row, col)


if __name__ == "__main__":
    main()