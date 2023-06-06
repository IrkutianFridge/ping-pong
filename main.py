from pygame import *
#okupoiu
win_width = 1000
win_height = 500

clock = time.Clock()
img_back = 'purple.png'
img_ball = 'ball.png'

ball_x = 10
ball_y = 10

display.set_caption("пинг понг")
font.init()
font1 = font.Font(None, 80)
font2 = font.Font(None, 80)

win_left = font1.render('left win!', True, (0, 0, 255))
win_right = font2.render('right win!', True, (255, 000, 0))


window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

finish = False
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
   def update_right(self):
       keys = key.get_pressed()
       if keys[K_DOWN] and self.rect.y < 350:
           self.rect.y += self.speed
       if keys[K_UP] and self.rect.y > -1:
           self.rect.y -= self.speed
   def update_left(self):
       keys = key.get_pressed()
       if keys[K_s] and self.rect.y < 350:
           self.rect.y += self.speed
       if keys[K_w] and self.rect.y > -1:
           self.rect.y -= self.speed


player_left = Player('plin.png', 0, 200, 50, 150, 10)
player_right = Player('plin.png', 950, 200, 50, 150, 10)
ball = Player('ball.png', 300, 200, 60, 60, 10)


while not game_over:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
           game_over = True
    if not finish:
        
        
        player_left.update_left()
        player_right.update_right()
        ball.update()
        
        player_left.reset() 
        player_right.reset()
        ball.reset()


        ball.rect.x += ball_x
        ball.rect.y += ball_y


        if ball.rect.y < 0:
                ball_y *= -1


        if ball.rect.x > 1000:
            window.blit(win_left,(370,200))
            
            finish = True
        if ball.rect.x < 0:
            window.blit(win_right,(370,200))
            
            finish = True



        if ball.rect.y > 460:
            ball_y *= -1
        
        if ball.rect.y < 1:
            ball_y *= -1
        


        if ball.rect.colliderect(player_left.rect) or ball.rect.colliderect(player_right.rect):
            ball_x *= -1

        display.update()
    clock.tick(50)
