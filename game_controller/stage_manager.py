import pygame
from utils.type import Color
from utils.enums import Stage
from game_of_life.menu import Menu
from game_of_life.grid import Grid
from utils.parameter import Parameter
from game_controller.button import Button
from game_controller.textfield import TextField


class StageManager:
    def __init__(self, screen: pygame.surface.Surface):
        self.screen: pygame.surface.Surface = screen

        # Initialize the grid
        self.tile_size: int = Parameter.tile_size
        self.grid = Grid()  # Play default / current grid
        self.cs_grid = Grid(True)  # Custom grid

        # Define the main menu
        self.main_menu = Menu([Button("PLAY"), Button("CUSTOM"), Button("SETTINGS")])

        # Initialize stage
        self.stage = Stage.INTRO

        # Initialize text fields
        x0 = 180
        y0 = 20
        h = 35
        self.text_fields = [
            TextField(screen, "Background Color:", x0, y0, str(Parameter.bg_color)),

            TextField(screen, "Grid Color:", x0, y0 + h, str(Parameter.grid_color)),

            TextField(screen, "Tile dead color:", x0, y0 + h * 2, str(Parameter.tile_dead_color)),
            TextField(screen, "Tile alive color:", x0, y0 + h * 3, str(Parameter.tile_alive_color)),

            TextField(screen, "Font color:", x0, y0 + h * 4, str(Parameter.font_color)),

            TextField(screen, "Rules:", x0, y0 + h * 5, str(Parameter.rules))
        ]

        self.save_btn = Button("SAVES CHANGES")
        self.save_btn.set_button_rect((screen.get_width() - 200) // 2, y0 + h * 12, 200, 50)

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
            for textfield in self.text_fields:
                textfield.draw()

            self.save_btn.draw(screen)

    def update_stage(self) -> None:
        if self.stage == Stage.INTRO:
            self.stage = self.main_menu.current_stage

        elif self.stage == Stage.PLAY:
            self.grid.update_state()

        elif self.stage == Stage.CUSTOM:
            self.grid.set_state(self.cs_grid.state)

        elif self.stage == Stage.SETTINGS:
            if self.save_btn.is_clicked:
                Parameter.bg_color = Color(*map(int, self.text_fields[0].input.split(",")))

                # Grid settings
                Parameter.grid_color = Color(*map(int, self.text_fields[3].input.split(",")))

                # Tile settings
                Parameter.tile_dead_color = Color(*map(int, self.text_fields[5].input.split(",")))
                Parameter.tile_alive_color = Color(*map(int, self.text_fields[6].input.split(",")))

                # Font settings
                Parameter.font_color = Color(*map(int, self.text_fields[9].input.split(",")))

                # Rules
                Parameter.rule = str(self.text_fields[10].input.strip())

    def handle_event(self, event: pygame.event.Event):
        if self.stage == Stage.INTRO:
            self.main_menu.handle_mouse_event()

        elif self.stage == Stage.SETTINGS:
            for textfield in self.text_fields:
                textfield.handle_typing(event)

            self.save_btn.handle_mouse_event()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.main_menu.previous_stage = self.main_menu.current_stage
            self.stage = Stage.INTRO
            self.main_menu.current_stage = Stage.INTRO
