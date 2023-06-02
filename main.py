from pygame import *

win_width = 1000
win_height = 500


background = 'purple.png'
img_ball = 'ball.png'


display.set_caption("пинг понг")


window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))


game_over = False 

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       sprite.Sprite.__init__(self)
 
 
       
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
 
 
       
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
 

class Player(GameSprite):
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed


#player_1 = Player()
#player_2 = Player()
#ball = Ball()


while not game_over:
    window.blit(background,(0,0))
    display.update()

time.delay(50)