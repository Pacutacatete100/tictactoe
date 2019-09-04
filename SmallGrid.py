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

    def click_board(self):
        print()

