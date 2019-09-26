import pygame


class SmallGrid:



    def __init__(self, start_X_horizontal_line_1, start_Y_horizontal_line_1, end_X_horizontal_line_1,
                 end_Y_horizontal_line_1,
                 start_X_horizontal_line_2, start_Y_horizontal_line_2, end_X_horizontal_line_2, end_Y_horizontal_line_2,
                 start_X_vertical_line_1, start_Y_vertical_line_1, end_X_vertical_line_1, end_Y_vertical_line_1,
                 start_X_vertical_line_2, start_Y_vertical_line_2, end_X_vertical_line_2, end_Y_vertical_line_2,
                 background):
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

        tlr = pygame.draw.rect(background, (255, 255, 255), (
            self.start_X_horizontal_line_1, self.start_Y_vertical_line_1,
            self.start_Y_horizontal_line_1 - self.start_Y_vertical_line_1,
            self.start_X_vertical_line_1 - self.start_X_horizontal_line_1), 0)
        self.top_left_rect = pygame.Rect(tlr)

        tmr = pygame.draw.rect(background, (255, 255, 255), (
            self.start_X_vertical_line_1 + 3, self.start_Y_vertical_line_1,
            self.start_X_vertical_line_2 - self.start_X_vertical_line_1 - 3,
            self.start_Y_horizontal_line_1 - self.start_Y_vertical_line_1), 0)
        self.top_middle_rect = pygame.Rect(tmr)

        trr = pygame.draw.rect(background, (255, 255, 255), (
            self.start_X_vertical_line_2 + 3, self.start_Y_vertical_line_1,
            self.start_Y_horizontal_line_1 - self.start_Y_vertical_line_1,
            self.start_X_vertical_line_1 - self.start_X_horizontal_line_1), 0)
        self.top_right_rect = pygame.Rect(trr)

        mlr = pygame.draw.rect(background, (255, 255, 255), (
            self.start_X_horizontal_line_1, self.start_Y_horizontal_line_1 + 3,
            self.start_Y_horizontal_line_1 - self.start_Y_vertical_line_1,
            self.start_Y_horizontal_line_2 - self.start_Y_horizontal_line_1 - 3), 0)
        self.middle_left_rect = pygame.Rect(mlr)

        mr = pygame.draw.rect(background, (255, 255, 255), (
            self.start_Y_horizontal_line_1 + 3, self.start_X_vertical_line_1 + 3,
            self.start_Y_horizontal_line_2 - self.start_Y_horizontal_line_1 - 3,
            self.start_Y_horizontal_line_2 - self.start_Y_horizontal_line_1 - 3), 0)
        self.middle_rect = pygame.Rect(mr)

        mrr = pygame.draw.rect(background, (255, 255, 255), (
            self.start_X_vertical_line_2 + 3, self.end_Y_horizontal_line_1 + 3,
            self.end_Y_horizontal_line_1 - self.start_Y_vertical_line_2,
            self.end_Y_horizontal_line_2 - self.end_Y_horizontal_line_1 - 3), 0)
        self.middle_right_rect = pygame.Rect(mrr)

        blr = pygame.draw.rect(background, (255, 255, 255), (
            self.start_X_horizontal_line_2, self.start_Y_horizontal_line_2 + 3,
            self.end_Y_vertical_line_1 - self.start_Y_horizontal_line_2,
            self.end_Y_vertical_line_1 - self.start_Y_horizontal_line_2), 0)
        self.bottom_left_rect = pygame.Rect(blr)

        bmr = pygame.draw.rect(background, (255, 255, 255), (
            self.end_X_vertical_line_1 + 3, self.start_Y_horizontal_line_2 + 3,
            self.end_X_vertical_line_2 - self.end_X_vertical_line_1 - 3,
            self.end_Y_vertical_line_2 - self.start_Y_horizontal_line_2), 0)
        self.bottom_middle_rect = pygame.Rect(bmr)

        brr = pygame.draw.rect(background, (255, 255, 255), (
            self.end_X_vertical_line_2 + 3, self.end_Y_horizontal_line_2 + 3,
            self.end_Y_vertical_line_2 - self.end_Y_horizontal_line_2,
            self.end_Y_vertical_line_2 - self.end_Y_horizontal_line_2), 0)
        self.bottom_right_rect = pygame.Rect(brr)

    def draw_small_grid(self, background):
        pygame.draw.line(background, (0, 0, 0), (self.start_X_horizontal_line_1, self.start_Y_horizontal_line_1),
                         (self.end_X_horizontal_line_1, self.end_Y_horizontal_line_1), 4)
        pygame.draw.line(background, (0, 0, 0), (self.start_X_horizontal_line_2, self.start_Y_horizontal_line_2),
                         (self.end_X_horizontal_line_2, self.end_Y_horizontal_line_2), 4)
        # vertical lines for small grid 1,1
        pygame.draw.line(background, (0, 0, 0), (self.start_X_vertical_line_1, self.start_Y_vertical_line_1),
                         (self.end_X_vertical_line_1, self.end_Y_vertical_line_1), 4)
        pygame.draw.line(background, (0, 0, 0), (self.start_X_vertical_line_2, self.start_Y_vertical_line_2),
                         (self.end_X_vertical_line_2, self.end_Y_vertical_line_2), 4)





