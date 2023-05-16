import pygame as pg
from pygame.locals import *
from pygame import Vector2, Rect, Color, Surface


class TouchKeys :

    def __init__( self, screen: Surface ) :
        self.screen = screen
        self.mouse = Rect(0, 0, 3, 3)
        self.is_touching = False
        self.arrow_rect_size = 0
        self.update_arrow_size()
        self.arrow_anchor = Vector2(0.8,0.6)
        self.is_commanding = False
        self.command = None

    def update_arrow_size( self ):
        self.arrow_rect_size = self.screen.get_width() * 0.07

    def get_events( self, events ) :

        for i in events :
            if i.type == FINGERDOWN or i.type == FINGERMOTION :
                self.is_touching = True
                self.mouse.center = i.x * self.screen.get_width(), i.y * self.screen.get_height()

            if i.type == FINGERUP:
                self.is_touching = False


    @property
    def arrow_up_rect( self ) :
        w,h = self.screen.get_size()
        anchor = self.arrow_anchor
        rect = Rect(0,0,self.arrow_rect_size,self.arrow_rect_size)

        rect.x = w * anchor.x
        rect.y = h * anchor.y

        return rect


    @property
    def arrow_up_right_rect( self ) :
        w, h = self.screen.get_size()
        anchor = self.arrow_anchor
        rect = Rect(0, 0, self.arrow_rect_size, self.arrow_rect_size)

        rect.x = w * anchor.x + rect.w * 1.1
        rect.y = h * anchor.y

        return rect


    @property
    def arrow_up_left_rect( self ) :
        w, h = self.screen.get_size()
        anchor = self.arrow_anchor
        rect = Rect(0, 0, self.arrow_rect_size, self.arrow_rect_size)

        rect.x = w * anchor.x - rect.w * 1.1
        rect.y = h * anchor.y

        return rect

    @property
    def arrow_down_rect( self ) :
        w, h = self.screen.get_size()
        anchor = self.arrow_anchor

        rect = Rect(0,0,self.arrow_rect_size,self.arrow_rect_size)

        rect.x = w * anchor.x
        rect.y = h * anchor.y + rect.h * 1.1

        return rect


    @property
    def arrow_right_rect( self ) :
        w, h = self.screen.get_size()
        anchor = self.arrow_anchor

        rect = Rect(0,0,self.arrow_rect_size,self.arrow_rect_size)

        rect.x = w * anchor.x + rect.w * 1.1
        rect.y = h * anchor.y + rect.h * 1.1

        return rect

    @property
    def arrow_left_rect( self ) :
        w, h = self.screen.get_size()
        anchor = self.arrow_anchor

        rect = Rect(0,0,self.arrow_rect_size,self.arrow_rect_size)

        rect.x = w * anchor.x - rect.w * 1.1
        rect.y = h * anchor.y + rect.h * 1.1

        return rect




    @property
    def arrows( self ) :
        return [self.arrow_up_rect, self.arrow_down_rect, self.arrow_right_rect,
            self.arrow_left_rect,self.arrow_up_right_rect,self.arrow_up_left_rect]


    def check_events( self ) :
        self.update_arrow_size()

        self.is_commanding = False
        for rect,command in zip(self.arrows,['u','d','r','l','ur','ul']) :
            if self.mouse.colliderect(rect) and self.is_touching :
                self.is_commanding = True
                self.command = command


    def render( self ) :

        for rect in self.arrows:
            color = 'black'
            if self.mouse.colliderect(rect) and self.is_touching:
                color = "red"

            pg.draw.rect(self.screen, color,rect, width=5)
