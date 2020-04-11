#! python 3
# k_means_clustering.py - Visualisation of K Means Clustering 
# Algorithm with Arcade.
import math
import random

import arcade
# import numpy as np


# Constant variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "K Means Clustering"
MARGINS = 20
NUM_OF_POINTS = 20
POINT_RADIUS = 10
POINT_DEFAULT_COLOR = arcade.color.WHITE
K = 3
MEANS_COLOR = [[random.randint(0, 256) for _ in range(3)] for _ in range(K)]
MEAN_ALPHA = 180


class Point():

	def __init__(self, x, y, color=POINT_DEFAULT_COLOR, cluster=None):
		self.x = x
		self.y = y
		self.color = color
		self.cluster = cluster

	def squared_distance_to(self, point):
		"""Returns the squared distance to the given point"""
		return (self.x - point.x) ** 2 + (self.y - point.y) ** 2

	def classify(self, k_means):
		"""Attach to closest mean's cluster"""
		distances = [(mean, self.squared_distance_to(mean)) for mean in k_means]
		closest_mean, _ = min(distances, key = lambda x: x[1])
		self.cluster = closest_mean.cluster
		self.color = closest_mean.color

	def update_position(self, x, y):
		"""Set new x and y"""
		self.x = x
		self.y = y


class KMeans(arcade.Window):
	"""Classify a random set of points using K Means Clustering Algorithm.

	2-D visualiser.
	"""
	def __init__(self, width, height, title):
		super().__init__(width, height, title)
		self.input_points = [Point(random.randint(MARGINS, SCREEN_WIDTH - MARGINS), 
							 random.randint(MARGINS, SCREEN_HEIGHT - MARGINS)) 
							 for _ in range(NUM_OF_POINTS)]
		self.k_means = []
		# Flags
		self.init = True
		self.clustered = False
		self.re_cluster = True

	def initiate_means(self, k=K):
		"""Randomly select k points from the input set
		
		to be the starting centroids.
		"""
		random_points = random.choices(self.input_points, k=k)
		for i, p in enumerate(random_points):
			self.k_means.append(
				Point(p.x, p.y, MEANS_COLOR[i], i))

	def classify_points(self):
		"""Cluster input_points"""
		cluster_changed = False
		for point in self.input_points:
			old_cluster = point.cluster
			point.classify(self.k_means)
			if point.cluster != old_cluster:
				cluster_changed = True
		if not cluster_changed:
			self.clustered = True

	def calculate_means(self):
		"""Update means position based on current clusters."""
		# Divide to clusters
		clusters = {}
		for i in range(K):
			clusters[i] = []
		for point in self.input_points:
			clusters[point.cluster].append(point)
		# calculate average x and y for each cluaster
		for cluster, points in clusters.items():
			if points:
				x = 0
				y = 0
				for p in points:
					x += p.x
					y += p.y
				self.k_means[cluster].update_position(x/len(points), y/len(points))
			else:
				self.k_means[cluster].update_position(None, None)

	def on_draw(self):

		arcade.start_render()
		# Draw points
		for point in self.input_points:
			arcade.draw_ellipse_filled(point.x, point.y, POINT_RADIUS, POINT_RADIUS, point.color)
		# Draw means
		if self.k_means:
			for mean in self.k_means:
				arcade.draw_rectangle_filled(mean.x, mean.y, POINT_RADIUS*1.5, POINT_RADIUS*1.5, mean.color + [MEAN_ALPHA])
			arcade.pause(2)

	def on_update(self, delta_time):

		if self.clustered:
			print('Clustering done!!')
			# arcade.pause(3)
			# self.k_means = []
			# self.clustered = False
			# for point in self.input_points:
			# 	point.cluster = None
			# self.re_cluster = True
		elif self.init:
			self.init = False
			return
		elif not self.k_means:
			self.initiate_means()
		else:
			if not self.re_cluster:
				self.calculate_means()
				self.re_cluster = True
			else:
				self.classify_points()
				self.re_cluster = False


def main():

	window = KMeans(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
	arcade.run()



if __name__ == '__main__':
	main()

