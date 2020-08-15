import pygame
from random import randint

BLACK = 25, 25, 25
WHITE = 250, 250, 250

score = 0

class Pelota(pygame.sprite.Sprite):
	def __init__(self, color, width, height):
		super(Pelota, self).__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(BLACK)
		self.image.set_colorkey(BLACK)

		pygame.draw.rect(self.image, color, [0, 0, width, height])

		#self.velocity = [randint(5, 8), randint(-5, 5)]
		self.velocity =[randint(2, 6), -10]
		# if 0 in self.velocity:
		# 	while 0 in self.velocity:
		# 		self.velocity[1] = randint(-5, 5)

		self.rect = self.image.get_rect()

	def update(self):
		self.rect.x += self.velocity[0]
		self.rect.y += self.velocity[1]

	def rebote(self):
		self.velocity[0] = -self.velocity[0]
		self.velocity[1] = randint(-10 - (int(score/10)), 10 - (int(score/10)))
		#self.velocity[1] = -self.velocity[1]
		if 0 in self.velocity:
			while 0 in self.velocity:
				self.velocity[1] = randint(-10 - (int(score/10)), 10 - (int(score/10)))

	def rebote_base(self, score):
		self.velocity[0] = randint(-6, 6)
		if 0 in self.velocity:
			while 0 in self.velocity:
				self.velocity[0] = randint(-6, 6)
		#self.velocity[0] = -self.velocity[0]
		self.velocity[1] = randint(-10 - (int(score/10)), -2 - (int(score/10)))
		print(self.velocity)
