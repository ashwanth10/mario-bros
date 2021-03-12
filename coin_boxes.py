import pygame as pg
from .. import setup
from .. import constants as c



class Coin_box(pg.sprite.Sprite):
    """Coin box sprite"""

    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['tile_set']
        self.image = self.get_image(384, 0 , 16, 16)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



    def get_image(self, x, y, width, height):
        image = pg.Surface([width, height]).convert()
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        image = pg.transform.scale(image,
                                   (int(rect.width*c.BRICK_SIZE_MULTIPLIER),
                                    int(rect.height*c.BRICK_SIZE_MULTIPLIER)))
        return image