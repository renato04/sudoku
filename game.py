import constants as c
import pygame
from sudoku_ui import SudokuUi

class Game:

    done = False
    sudoku = SudokuUi()
    
    def start(self):
        pygame.init()
        

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True        

    def draw(self):
        self.sudoku.draw()
        pygame.display.flip()

    def play(self):
        self.start()
        while not self.done:
           self.update()
           self.draw()

g = Game()
g.play()
            

            
      

          


    
    
