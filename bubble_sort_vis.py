#! python 3
# bubble_sort_vis.py - Visualisation of Bubble Sort Algorithm
# with Arcade.

import arcade
import numpy as np
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Bubble Sort"
BAR_COLOR = arcade.color.BLUSH
MOVING_BAR_COLOR = arcade.color.BLUE
BAR_WIDTH = 15
START_X = 25
START_Y = 50
SPACE = 5


class Bar:

    def __init__(self, height, color):
        self.height = height
        self.color = color


class Array:

    def __init__(self, size=50):
        self.array = [Bar(np.random.randint(10, 500), BAR_COLOR) for _ in
                      range(size)]
        # index vars for sorting
        self.i = 0
        self.j = 0

    def swap(self, a, b):
        """Swaps between 2 items [a,b] of own array"""
        temp = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = temp

    def bubble_sort(self):
        # print(self.j)
        self.array[self.j].color = MOVING_BAR_COLOR
        # if self.j > 0:
        # 	self.array[self.j - 1].color = BAR_COLOR
        # arcade.pause(5)
        if self.i < len(self.array) - 1:
            if self.j < len(self.array) - self.i - 1:
                if self.array[self.j].height > self.array[self.j + 1].height:
                    self.swap(self.j, self.j + 1)
                # 	self.array[self.j + 1].color = MOVING_BAR_COLOR
                # 	self.array[self.j].color = BAR_COLOR
                # self.array[self.j].color = BAR_COLOR
                else:
                    self.array[self.j].color = BAR_COLOR
                    self.array[self.j + 1].color = MOVING_BAR_COLOR
                self.j += 1
            else:
                self.j = 0
                self.i += 1
                self.array[self.j].color = MOVING_BAR_COLOR


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.array = Array()

    def on_draw(self):
        arcade.start_render()
        for i, bar in enumerate(self.array.array):
            left = START_X + i * BAR_WIDTH + SPACE
            right = START_X + (i + 1) * BAR_WIDTH
            top = START_Y + self.array.array[i].height
            bottom = START_Y
            arcade.draw_lrtb_rectangle_filled(left, right, top, bottom,
                                              bar.color)

    # arcade.pause(0.2)

    def on_update(self, delta_time):
        self.array.bubble_sort()


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
# bars = [Bar(np.random.randint(0,256), np.random.randint(0,256,3)) for _ in range(2)]
# for bar in bars:
# 	print(bar.height, bar.color)
