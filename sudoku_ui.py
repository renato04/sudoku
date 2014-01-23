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
        self.draw_board()
#        draw_panel()
#        draw_cursor()

    def draw_background(self):
        pygame.draw.rect(self.screen, (255,255,255),
                         pygame.Rect(0, 0,
                                     c.screen_width, c.screen_height))
    def draw_board(self):
#        self.draw_cell_backgrounds()
        self.draw_grid()
        self.draw_numbers()

    def draw_grid(self):

        for i in range(0, c.Size + 1):

            
        
    
    
