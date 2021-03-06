import pygame
from pygame import *
import levels as lv

WIN_WIDTH = 800
WIN_HEIGHT = 640
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0
CAMERA_SLACK = 30
CURRENTLEVEL = 0
PLATFORMS = []

def Main():
	global cameraX , cameraY , ENTITIES
	pygame.init()

	## Setup Display and caption ##
	screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
	pygame.display.set_caption("<GAME TITLE>")
	timer = pygame.time.Clock()
	## Create and set movement flags to false ##
	up = down = left = right = running = False

	## Background ##
	bg = Surface((32,32))
	bg.convert()
	bg.fill(Color("#000000"))

	#Sprite group
	ENTITIES = pygame.sprite.Group()

	## Level building
	player = buildlevel()
	camera = Camera(simple_camera, 1408, 800)

	while 1:
		timer.tick(60)

		for e in pygame.event.get():
			if e.type == QUIT: raise SystemExit, "QUIT"
			if e.type == KEYDOWN and e.key == K_ESCAPE:
			    raise SystemExit, "ESCAPE"
			if e.type == KEYDOWN and e.key == K_UP:
			    up = True
			if e.type == KEYDOWN and e.key == K_DOWN:
			    down = True
			if e.type == KEYDOWN and e.key == K_LEFT:
			    left = True
			if e.type == KEYDOWN and e.key == K_RIGHT:
			    right = True
			if e.type == KEYDOWN and e.key == K_SPACE:
			    running = True

			if e.type == KEYUP and e.key == K_UP:
			    up = False
			if e.type == KEYUP and e.key == K_DOWN:
			    down = False
			if e.type == KEYUP and e.key == K_RIGHT:
			    right = False
			if e.type == KEYUP and e.key == K_LEFT:
			    left = False

		# draw background
		for y in range(32):
			for x in range(32):
				screen.blit(bg, (x * 32, y * 32))

		camera.update(player)

	# update player, draw everything else
		player.update(up, down, left, right, running, PLATFORMS)
		for e in ENTITIES:
			screen.blit(e.image, camera.apply(e))

		pygame.display.update()

def buildlevel():
	ENTITIES.empty
	PLATFORMS = []
	x = y = 0
	leveldata = lv.fetch_level(CURRENTLEVEL)
	level = leveldata[0]
	for row in level:
		for col in row:
			if col == "P":
				p = Platform(x, y)
				PLATFORMS.append(p)
				ENTITIES.add(p)
			if col == "E":
				e = ExitBlock(x, y)
				PLATFORMS.append(e)
				ENTITIES.add(e)
			x += 32
		y += 32
		x = 0
	player = Player(leveldata[1],leveldata[2])
	ENTITIES.add(player)
	return player

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)

def simple_camera(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)


class Player(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.image = Surface((32,32))
        self.image.fill(Color("#0000FF"))
        self.image.convert()
        self.rect = Rect(x, y, 32, 32)

    def update(self, up, down, left, right, running, platforms):
        if up:
            # only jump if on the ground
            if self.onGround:
                self.yvel -= 10
        if down:
            pass
        if running:
            self.xvel = 12
        if left:
            self.xvel = -8
        if right:
            self.xvel = 8
        if not self.onGround:
            # only accelerate with gravity if in the air
            self.yvel += 0.3
            # max falling speed
            if self.yvel > 100: 
                self.yvel = 100
        if not(left or right):
            self.xvel = 0
        # increment in x direction
        self.rect.left += self.xvel
        # do x-axis collisions
        self.collide(self.xvel, 0, platforms)
        # increment in y direction
        self.rect.top += self.yvel
        # assuming we're in the air
        self.onGround = False;
        # do y-axis collisions
        self.collide(0, self.yvel, platforms)

    def collide(self, xvel, yvel, platforms):
        for p in platforms:
            if pygame.sprite.collide_rect(self, p):
                if isinstance(p, ExitBlock):
                    pygame.event.post(pygame.event.Event(QUIT))
                if xvel > 0:
                    self.rect.right = p.rect.left
                    print "collide right"
                if xvel < 0:
                    self.rect.left = p.rect.right
                    print "collide left"
                if yvel > 0:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.yvel = -.1
class Platform(Entity):
    def __init__(self, x, y):
        Entity.__init__(self)
        self.image = Surface((32, 32))
        self.image.convert()
        self.image.fill(Color("#DDDDDD"))
        self.rect = Rect(x, y, 32, 32)

    def update(self):
        pass

class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image.fill(Color("#0033FF"))


if __name__ == "__main__":
    Main()