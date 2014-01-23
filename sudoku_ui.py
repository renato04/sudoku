from sudoku import Sudoku
import pygame
import constants as c

class SudokuUi:

    screen = pygame.display.set_mode((c.screen_width,c.screen_height))
    
    def __init__(self):
        self.sudoku = Sudoku()
        self.over = False
        self.selected_x = -1
        self.selected_y = -1
        self.wating_number = False

    def draw(self):
        self.draw_background()
#        draw_board()
#        draw_panel()
#        draw_cursor()

    def draw_background(self):
        pygame.draw.rect(self.screen, (255,255,255),
                         pygame.Rect(0, 0,
                                     c.screen_width, c.screen_height))
        
##        pygame.draw.rect(self.screen, (0, 128, 255), pygame.Rect(30, 30, 60, 60))        
    
