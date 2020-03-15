#! python 3
# bubble_sort_vis.py - Visualisation of Bubble Sort Algorithm
# with Arcade.

import arcade
import numpy as np
import time


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Bubble Sort"
bar_color = arcade.color.BLUSH
bar_width = 15
start_x = 25
start_y = 50
space = 5
i = 0
j = 0


def swap(arr, i, j):
	"""Gets array and 2 indices, switches between items in position i and j."""
	temp = arr[i]
	arr[i] = arr[j]
	arr[j] = temp


class MyGame(arcade.Window):

	def __init__(self, width, height, title):
		super().__init__(width, height, title)
		self.array = np.random.randint(10, 500, 50)


	def on_draw(self):

		arcade.start_render()
		for i, size in enumerate(self.array):
			left = start_x + i * bar_width + space
			right = start_x + (i+1) * bar_width
			top = start_y + self.array[i]
			bottom = start_y
			arcade.draw_lrtb_rectangle_filled(left, right, top, bottom, bar_color)


	def on_update(self, delta_time):

		if i < len(self.array): # in range(len(self.array)):
			for j in range(len(self.array) - i - 1):
				if self.array[j] > self.array[j + 1]:
					swap(self.array, j, j + 1)
		i += 1



def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    # window.start_snowfall()
    arcade.run()


if __name__ == "__main__":
    print(i)
    main()