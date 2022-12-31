import pygame
from utils.enums import Stage
from game_of_life.menu import Menu
from game_of_life.grid import Grid
from utils.parameter import Parameter
from game_controller.button import Button
from game_controller.textfield import TextField


class StageManager:
    def __init__(self):
        # Initialize the grid
        self.tile_size: int = Parameter.tile_size
        self.grid = Grid(Parameter.grid_cols, Parameter.grid_rows, Parameter.tile_size)  # Random / default grid
        self.cs_grid = Grid(Parameter.grid_cols, Parameter.grid_rows, Parameter.tile_size, True)  # Custom grid

        # Define the main menu
        self.main_menu = Menu([Button("PLAY"), Button("CUSTOM"), Button("SETTINGS")])

        # Initialize stage
        self.stage = Stage.INTRO

        #  self.textfield = TextField(screen, "Test :", 50, 100)

    def draw_stage(self, screen: pygame.surface.Surface) -> None:
        if self.stage == Stage.INTRO:
            w = 200
            h = 50
            x0 = (screen.get_width() - w) // 2
            y0 = (screen.get_height() - h) // 2

            self.main_menu.update_button_rect(x0, y0, w, h)
            self.main_menu.draw(screen)

        elif self.stage == Stage.PLAY:
            self.grid.draw_state(screen)

        elif self.stage == Stage.CUSTOM:
            self.cs_grid.draw_state(screen)

        elif self.stage == Stage.SETTINGS:
            pass

    def update_stage(self) -> None:
        if self.stage == Stage.INTRO:
            self.main_menu.handle_mouse_event()
            self.stage = self.main_menu.current_stage

        elif self.stage == Stage.PLAY:
            self.grid.update_state()

        elif self.stage == Stage.CUSTOM:
            self.grid.set_state(self.cs_grid.state)

        elif self.stage == Stage.SETTINGS:
            pass

        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            self.main_menu.previous_stage = self.main_menu.current_stage
            self.stage = Stage.INTRO
            self.main_menu.current_stage = Stage.INTRO
