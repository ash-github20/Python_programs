import pygame
pygame.init()
pygame.mixer.init()
screen_width=600
screen_height=640

gameWindow = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("TIC TAC TOE")
X=pygame.image.load('D:\Python\Python programs\Tic_Tac_Toe\X.png')
O=pygame.image.load('D:\Python\Python programs\Tic_Tac_Toe\O.png')
red = (255,0,0)

start_on = True
turn=0

def start_game():
    exit_game = False
    game_over = False

    FPS = 60
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('Snake Chan',15)
    font1 = pygame.font.SysFont('Snake Chan',35)
    board = [[0,0,0],[0,0,0],[0,0,0]]
    return exit_game,game_over,FPS,clock,font,font1,board

exit_game,game_over,FPS,clock,font,font1,board = start_game()

def win_check(player):
    for i in range(3):
        if board[0][i]==board[1][i]==board[2][i]==player:
            return 'vertical'
        elif board[i][0]==board[i][1]==board[i][2]==player:
            return 'horizontal'

    if board[0][0]==board[1][1]==board[2][2]==player or board[2][0]==board[1][1]==board[2][0]==player:
        return 'diagonal'
    
    if 0 not in board[0] and 0 not in board[1] and 0 not in board[2]:
        return 'draw'
    return False

def drawboard():
    pygame.draw.line(gameWindow, (0,0,0),(200,0),(200,600),3)
    pygame.draw.line(gameWindow, (0,0,0),(400,0),(400,600),3)
    pygame.draw.line(gameWindow, (0,0,0),(0,200),(600,200),3)
    pygame.draw.line(gameWindow, (0,0,0),(0,400),(600,400),3)
    pygame.draw.line(gameWindow, (0,0,0),(0,600),(600,600),3)
    pygame.display.update()

def put_text(text,color,x,y,font):
    text_screen = font.render(text,True,color)
    gameWindow.blit(text_screen,[x,y])



gameWindow.fill(255,255,255)
while not exit_game:
    for _ in pygame.event.get():
        if pygame.event.type == pygame.QUIT:
            exit_game = True
        elif pygame.event.type == pygame.MOUSEBUTTONDOWN:
            click_position = pygame.event.posi
            click_position = (200 * (click_position[0]//200), 200 * (click_position[1]//200))
            
