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
    pieces = ['br', 'bb', 'bn', 'bq', 'bk', 'bp', 'wb', 'wn', 'wq', 'wk', 'wp', 'wr'] # names of files to load
    for piece in pieces:
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("pieces/" + str(piece) + ".png"), (SQ_SIZE, SQ_SIZE))


def draw_game(screen, game, move=[]): 
    '''draws the board and peaces'''
    draw_board(screen, move) # helper function
    draw_pieces(screen, game) # helper function

# helper functions for draw_game
def draw_board(screen, move):
    '''draws the board'''
    colors = [pygame.Color('white'), pygame.Color('gray')]
    for i in range(DIMENSIONS):
        for j in range(DIMENSIONS):
            color = colors[((i+j) % 2)]
            pygame.draw.rect(screen, color, pygame.Rect(j*SQ_SIZE, i*SQ_SIZE, SQ_SIZE, SQ_SIZE))

def draw_pieces(screen, game):
    '''draws the pieces'''
    for i in range(DIMENSIONS):
        for j in range(DIMENSIONS):
            match game.board[i][j]:
                case 'b':
                    screen.blit(IMAGES['bb'], (j*SQ_SIZE, i*SQ_SIZE))
                case 'n':
                    screen.blit(IMAGES['bn'], (j*SQ_SIZE, i*SQ_SIZE))
                case 'q':
                    screen.blit(IMAGES['bq'], (j*SQ_SIZE, i*SQ_SIZE))
                case 'k':
                    screen.blit(IMAGES['bk'], (j*SQ_SIZE, i*SQ_SIZE))
                case 'p':
                    screen.blit(IMAGES['bp'], (j*SQ_SIZE, i*SQ_SIZE))
                case 'r':
                    screen.blit(IMAGES['br'], (j*SQ_SIZE, i*SQ_SIZE))
                case 'B':
                    screen.blit(IMAGES['wb'], (j*SQ_SIZE, i*SQ_SIZE))
                case 'N':
                    screen.blit(IMAGES['wn'], (j*SQ_SIZE, i*SQ_SIZE))
                case 'Q':
                    screen.blit(IMAGES['wq'], (j*SQ_SIZE, i*SQ_SIZE))
                case 'K':
                    screen.blit(IMAGES['wk'], (j*SQ_SIZE, i*SQ_SIZE))
                case 'P':
                    screen.blit(IMAGES['wp'], (j*SQ_SIZE, i*SQ_SIZE))
                case 'R':
                    screen.blit(IMAGES['wr'], (j*SQ_SIZE, i*SQ_SIZE))
                case ' ':
                    pass


def main():
    '''main driver. handles user input and updates the game state'''
    # only done once before the while loop
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    game_state = engine.game()
    load_images() 
    running = True
    mouse_click = []
    # screen.set_caption(str(game_state.turn) + " turn", icontitle=None)

    while running:
        move = []
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # ends the game
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                location = (location[1] // SQ_SIZE, location[0] // SQ_SIZE)
                mouse_click.append(location) # returns a tuple (x, y)
                if len(mouse_click) == 2:
                    game_state.move(mouse_click[0], mouse_click[1])
                    mouse_click.clear()
                elif len(mouse_click) == 1:
                    move = game_state.show_move(mouse_click[0][1], mouse_click[0][1])
            
        draw_game(screen, game_state, move)
        clock.tick(MAX_FPS)
        pygame.display.flip()



if __name__ == "__main__":
    main()