import pygame
from pygame.locals import *
from base import Base
from pelota import Pelota
from ladrillo import Ladrillo



BLACK = (25,25,25)
WHITE = (250,250,250)
DARKBLUE = (36,90,190)
LIGHTBLUE = (0,176,240)
RED = (240,0,0)
ORANGE = (250,100,0)
YELLOW = (245,245,0)

COLOR1 = (245,0,0)
COLOR2 = (245,50,0)
COLOR3 = (245,75,0)
COLOR4 = (245,100,0)
COLOR5 = (245,125,0)
COLOR6 = (245,150,0)
COLOR7 = (245,175,0)
COLOR8 = (245,200,0)
COLOR9 = (245,225,0)
COLOR10 = (245,250,0)
colores = [COLOR1, COLOR2, COLOR3, COLOR4, COLOR5, COLOR6, COLOR7, COLOR8, COLOR9, COLOR10]

def main():
	pygame.init()
	
	score = 0
	lives = 3

	size = (1080, 720)
	screen = pygame.display.set_mode(size)
	pygame.display.set_caption("Breaker game")

	lista_sprites = pygame.sprite.Group()

	base = Base(LIGHTBLUE, 100, 10)
	base.rect.x = (size[0]/2) - 50
	base.rect.y = 700

	bola = Pelota(WHITE, 10, 10)
	bola.rect.x = 540
	bola.rect.y = 700

	los_ladrillos = pygame.sprite.Group()
	# for i in range(9):
	# 	ladrillo = Ladrillo(RED, 100, 30)
	# 	ladrillo.rect.x = 50 + i* 110
	# 	ladrillo.rect.y = 60
	# 	lista_sprites.add(ladrillo)
	# 	los_ladrillos.add(ladrillo)
	# for i in range(9):
	# 	ladrillo = Ladrillo(ORANGE, 100, 30)
	# 	ladrillo.rect.x = 50 + i* 110
	# 	ladrillo.rect.y = 100
	# 	lista_sprites.add(ladrillo)
	# 	los_ladrillos.add(ladrillo)
	# for i in range(9):
	# 	ladrillo = Ladrillo(YELLOW, 100, 30)
	# 	ladrillo.rect.x = 50 + i* 110
	# 	ladrillo.rect.y = 140
	# 	lista_sprites.add(ladrillo)
	# 	los_ladrillos.add(ladrillo)
	altolinea = 60

	for c in colores:
		for i in range(9):
			ladrillo = Ladrillo(c, 100, 30)
			ladrillo.rect.x = 50 + i* 110
			ladrillo.rect.y = altolinea
			lista_sprites.add(ladrillo)
			los_ladrillos.add(ladrillo)
		altolinea +=40

	lista_sprites.add(base)
	lista_sprites.add(bola)

	running = True
	clock = pygame.time.Clock()

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT]:
			base.move_left(10)
		if keys[pygame.K_RIGHT]:
			base.move_right(10) 

		lista_sprites.update()

		if bola.rect.x>=size[0]-10:
			bola.velocity[0] = -bola.velocity[0]
		if bola.rect.x<=0:
			bola.velocity[0] = -bola.velocity[0]
		if bola.rect.y>size[1]-10:
			bola.velocity[1] = -bola.velocity[1]
			lives-=1
			bola.rect.x = 540
			bola.rect.y = 690
			base.rect.x = (size[0]/2) - 50
			base.rect.y = 700
			pygame.time.wait(1000)
			# if lives < 1:
			# 	for ladrillo in los_ladrillos:
			# 		ladrillo.kill()
			# 		pygame.display.update()
			# 	print("ladrillos fuera")
			# 	font = pygame.font.Font(None, 72)
			# 	text = font.render("GAME OVER", True, RED)
			# 	screen.blit(text, (20,10))
			# 	pygame.display.flip()
			# 	#pygame.time.wait(60000)
			# 	print("GAME OVER")

				#running = False
				# font = pygame.font.Font(None, 72)
				# text = font.render("GAME OVER", True, RED)
				# screen.blit(text, (20,10))
				# pygame.display.flip()

		if bola.rect.y<40:
			bola.velocity[1] = -bola.velocity[1]

		if pygame.sprite.collide_mask(bola, base):
			#bola.rect.x -= bola.velocity[0]
			bola.rect.y -= bola.velocity[1]
			bola.rebote_base(score)
			print(score)

		ladrillos_tocados = pygame.sprite.spritecollide(bola, los_ladrillos, False)
		for ladrillo in ladrillos_tocados:
			bola.rebote()
			score+=1
			print(bola.velocity)
			ladrillo.kill()
		

		screen.fill(BLACK)
		pygame.draw.line(screen, WHITE, [0, 38], [1080, 38], 2)

		font = pygame.font.Font(None, 36)
		text = font.render("Score: " + str(score), 1, WHITE)
		screen.blit(text, (20, 10))
		text = font.render("Lives: " + str(lives), 1, WHITE)
		screen.blit(text, (size[0]-110, 10))

		if len(los_ladrillos) == 0 and lives > 0:
			font = pygame.font.Font(None, 72)
			text = font.render("NIVEL SUPERADO", 1, WHITE)
			screen.blit(text, (((size[0]/2) - text.get_width() // 2, (size[1]/2) - text.get_height())))
			font = pygame.font.Font(None, 36)
			text = font.render("Haz click para salir", True, WHITE)
			screen.blit(text, (((size[0]/2) - text.get_width() // 2, (size[1]/2) + text.get_height() * 2)))
			text = font.render("Pulsa \"espacio\" para jugar otra vez", True, WHITE)
			screen.blit(text, (((size[0]/2) - text.get_width() // 2, (size[1]/2) + text.get_height() * 4)))
			pygame.display.update()
			#pygame.time.wait(3000)

			#running = False
			clock.tick(10)

			if event.type == MOUSEBUTTONDOWN:
				running = False
			elif event.type == KEYDOWN:
				if event.key == pygame.K_SPACE:
					pygame.time.delay(1000)
					main()

		if lives < 1:
			for ladrillo in los_ladrillos:
				ladrillo.kill()
				#pygame.display.update()
			print("ladrillos fuera")
			bola.kill()
			font = pygame.font.Font(None, 72)
			text = font.render("GAME OVER", True, WHITE)
			screen.blit(text, (((size[0]/2) - text.get_width() // 2, (size[1]/2) - text.get_height())))
			font = pygame.font.Font(None, 36)
			text = font.render("Haz click para salir", True, WHITE)
			screen.blit(text, (((size[0]/2) - text.get_width() // 2, (size[1]/2) + text.get_height() * 2)))
			text = font.render("Pulsa \"espacio\" para jugar otra vez", True, WHITE)
			screen.blit(text, (((size[0]/2) - text.get_width() // 2, (size[1]/2) + text.get_height() * 4)))
			pygame.display.update()
			
			#pygame.time.delay(6000)
			print("GAME OVER")
			clock.tick(10)

			if event.type == MOUSEBUTTONDOWN:
				print("He hecho clic")
				running = False
			elif event.type == KEYDOWN:
				if event.key == pygame.K_SPACE:
					pygame.time.delay(1000)
					main()

			#running = False

		lista_sprites.draw(screen)

		pygame.display.flip()

		clock.tick(60)

pygame.quit()

if __name__ == '__main__':
	main()
