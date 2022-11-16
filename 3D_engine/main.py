""" Main file for 3D engine"""

import pygame as pg


class SoftwareRender:
    """
    A constructor
    ...
    Attributes
    ----------
    res, widht, height : tuple, int, int
        resolution of the screen: res=(width, height)
    h_width, h_height: int, int
        half of the lenght of the screen dimensions
    fps: int
        frame per seconds
    screen: pygame object
        the screen itself
    clock: pygame object
    ...
    """
    def __init__(self):
        """
        Initializing the object
        """
        pg.init()
        self.res = self.width, self.height = 1600, 900
        self.h_width, self.h_height = self.width // 2, self.height // 2
        self.fps = 60 # frame per seconds
        self.screen = pg.display.set_mode(self.res)
        self.clock = pg.time.Clock()

    def draw(self):
        """Generating the screen"""
        self.screen.fill(pg.Color('darkslategray'))

    def run(self):
        """Running the programm"""
        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.fps)


if __name__ == '__main__':
    app = SoftwareRender()
    app.run()
