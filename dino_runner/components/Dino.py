import pygame


from pygame.sprite import Sprite

from dino_runner.utils.constants import  RUNNING,JUMPING,DUCKING

class Dino(Sprite): 
    X_pos=80
    Y_pos=310
    Duck_Y_pos=344
    jumpSpeed= 8.5
    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos
        self.step_ind = 0
        self.dRun = True
        self.dJump = False
        self.dDuck = False
        self.velJump = self.jumpSpeed

    def update(self, user_input):
        if self.dRun:
            self.Run()
        elif self.dJump:
            self.Jump()
        elif self.dDuck:
            self.Duck()

        if user_input[pygame.K_UP]:
            self.dJump=True
            self.dRun=False
            self.dDuck=False
        elif user_input[pygame.K_DOWN]:
            self.dJump=False
            self.dRun=False
            self.dDuck = True
        elif not self.dJump and not self.dDuck:
            self.dJump=False
            self.dRun=True
            self.dDuck=False

        if self.step_ind >= 10:
            self.step_ind = 0

    def Run(self):
        if self.step_ind<=5:
            self.image=RUNNING[0]
        
        else:
            self.image=RUNNING[1]
            
        self.dino_rect = self.image.get_rect() 
        self.dino_rect.x = self.X_pos
        self.dino_rect.y = self.Y_pos
        self.step_ind += 1

    def draw(self, screen: pygame.surface):
        screen.blit(self.image, (80,310))
    
    def Jump(self):
        self.image = JUMPING
        if self.dJump:
            self.dino_rect.y -= self.velJump * 4
            self.velJump -= 0.8
        
        if self.velJump < -self.jumpSpeed:
            self.dino_rect.y = self.Y_pos
            self.dJump = False
            self.velJump=self.jumpSpeed
    
    def Duck(self):
            if self.step_ind<=5:
                self.image=DUCKING[0]
            
            else:
                self.image=DUCKING[1]
                
            self.dino_rect = self.image.get_rect() 
            self.dino_rect.x = self.X_pos
            self.dino_rect.y = self.Duck_Y_pos
            self.step_ind += 1
            self.dDuck =False
