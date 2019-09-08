import pygame

class SmallGrid:

    def __init__(self, start_X_horizontal_line_1, start_Y_horizontal_line_1, end_X_horizontal_line_1, end_Y_horizontal_line_1,
                 start_X_horizontal_line_2, start_Y_horizontal_line_2, end_X_horizontal_line_2, end_Y_horizontal_line_2,
                 start_X_vertical_line_1, start_Y_vertical_line_1, end_X_vertical_line_1, end_Y_vertical_line_1,
                 start_X_vertical_line_2, start_Y_vertical_line_2, end_X_vertical_line_2, end_Y_vertical_line_2):

        self.start_X_horizontal_line_1 = start_X_horizontal_line_1
        self.start_Y_horizontal_line_1 = start_Y_horizontal_line_1
        self.end_X_horizontal_line_1 = end_X_horizontal_line_1
        self.end_Y_horizontal_line_1 = end_Y_horizontal_line_1
        self.start_X_horizontal_line_2 = start_X_horizontal_line_2
        self.start_Y_horizontal_line_2 = start_Y_horizontal_line_2
        self.end_X_horizontal_line_2 = end_X_horizontal_line_2
        self.end_Y_horizontal_line_2 = end_Y_horizontal_line_2
        self.start_X_vertical_line_1 = start_X_vertical_line_1
        self.start_Y_vertical_line_1 = start_Y_vertical_line_1
        self.end_X_vertical_line_1 = end_X_vertical_line_1
        self.end_Y_vertical_line_1 = end_Y_vertical_line_1
        self.start_X_vertical_line_2 = start_X_vertical_line_2
        self.start_Y_vertical_line_2 = start_Y_vertical_line_2
        self.end_X_vertical_line_2 = end_X_vertical_line_2
        self.end_Y_vertical_line_2 = end_Y_vertical_line_2

    def draw_small_grid(self, background):
        pygame.draw.line(background, (0, 0, 0), (self.start_X_horizontal_line_1, self.start_Y_horizontal_line_1), (self.end_X_horizontal_line_1, self.end_Y_horizontal_line_1), 4)
        pygame.draw.line(background, (0, 0, 0), (self.start_X_horizontal_line_2, self.start_Y_horizontal_line_2), (self.end_X_horizontal_line_2, self.end_Y_horizontal_line_2), 4)
        # vertical lines for small grid 1,1
        pygame.draw.line(background, (0, 0, 0), (self.start_X_vertical_line_1, self.start_Y_vertical_line_1), (self.end_X_vertical_line_1, self.end_Y_vertical_line_1), 4)
        pygame.draw.line(background, (0, 0, 0), (self.start_X_vertical_line_2, self.start_Y_vertical_line_2), (self.end_X_vertical_line_2, self.end_Y_vertical_line_2), 4)

        top_left_rect = pygame.draw.rect(background, (255, 255, 255), (
            self.start_X_horizontal_line_1, self.start_Y_vertical_line_1,
            self.start_Y_horizontal_line_1 - self.start_Y_vertical_line_1,
            self.start_X_vertical_line_1 - self.start_X_horizontal_line_1), 0)
        top_middle_rect = pygame.draw.rect(background, (255, 255, 255), (
            self.start_X_vertical_line_1 + 3, self.start_Y_vertical_line_1,
            self.start_X_vertical_line_2 - self.start_X_vertical_line_1 - 3,
            self.start_Y_horizontal_line_1 - self.start_Y_vertical_line_1), 0)
        top_right_rect = pygame.draw.rect(background, (255, 255, 255), (
            self.start_X_vertical_line_2 + 3, self.start_Y_vertical_line_1,
            self.start_Y_horizontal_line_1 - self.start_Y_vertical_line_1,
            self.start_X_vertical_line_1 - self.start_X_horizontal_line_1), 0)

        middle_left_rect = pygame.draw.rect(background, (255, 255, 255), (
            self.start_X_horizontal_line_1, self.start_Y_horizontal_line_1 + 3,
            self.start_Y_horizontal_line_1 - self.start_Y_vertical_line_1,
            self.start_Y_horizontal_line_2 - self.start_Y_horizontal_line_1 - 3), 0)
        middle_rect = pygame.draw.rect(background, (255, 255, 255), (
            self.start_Y_horizontal_line_1 + 3, self.start_X_vertical_line_1 + 3,
            self.start_Y_horizontal_line_2 - self.start_Y_horizontal_line_1 - 3,
            self.start_Y_horizontal_line_2 - self.start_Y_horizontal_line_1 - 3), 0)
        middle_right_rect = pygame.draw.rect(background, (255, 255, 255), (
            self.start_X_vertical_line_2 + 3, self.end_Y_horizontal_line_1 + 3,
            self.end_Y_horizontal_line_1 - self.start_Y_vertical_line_2,
            self.end_Y_horizontal_line_2 - self.end_Y_horizontal_line_1 - 3), 0)

        bottom_left_rect = pygame.draw.rect(background, (255, 255, 255), (
            self.start_X_horizontal_line_2, self.start_Y_horizontal_line_2 + 3,
            self.end_Y_vertical_line_1 - self.start_Y_horizontal_line_2,
            self.end_Y_vertical_line_1 - self.start_Y_horizontal_line_2), 0)
        bottom_middle_rect = pygame.draw.rect(background, (255, 255, 255), (
            self.end_X_vertical_line_1 + 3, self.start_Y_horizontal_line_2 + 3,
            self.end_X_vertical_line_2 - self.end_X_vertical_line_1 - 3,
            self.end_Y_vertical_line_2 - self.start_Y_horizontal_line_2), 0)
        bottom_right_rect = pygame.draw.rect(background, (255, 255, 255), (
            self.end_X_vertical_line_2 + 3, self.end_Y_horizontal_line_2 + 3,
            self.end_Y_vertical_line_2 - self.end_Y_horizontal_line_2,
            self.end_Y_vertical_line_2 - self.end_Y_horizontal_line_2), 0)

        """
        -TODO: 
            *draw X or O with:
                mpos = pygame.mouse.get_pos() # Get mouse position
                if spRect.collidepoint(mpos): # Check if position is in the rect
                    #Code for what you wish the click to do
                    
            figure out why that method is not working (maybe at the moment rects arent objects)
        """

    def click_board(self, background):

        mouse_position = pygame.mouse.get_pos()



