import pygame

BLACK = (25, 25, 25)

class Base(pygame.sprite.Sprite):

	def __init__(self, color, width, height):
		super().__init__()

		self.width = width
		self.image = pygame.Surface([width, height])
		self.image.fill(BLACK)
		self.image.set_colorkey(BLACK)

		pygame.draw.rect(self.image, color, [0, 0, width, height])

		self.rect = self.image.get_rect()

	def move_left(self, pixels):
		self.rect.x -= pixels
		if self.rect.x < 0:
			self.rect.x = 0

	def move_right(self, pixels):
		self.rect.x += pixels
		if self.rect.x > 1080-self.width:
			self.rect.x = 1080-self.width