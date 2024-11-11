
import pygame
from spritesheet import SpriteSheet

class Player(pygame.sprite.Sprite):
    def __init__(self, sprite_sheet: SpriteSheet,speed=1):
        super().__init__()
        self.sprite_sheet = sprite_sheet
        self.animations = sprite_sheet.animations
        self.direction = "right" 
        self.current_animation = "idle"
        self.current_frame = 0
        self.image = self.animations[self.current_animation][self.current_frame]
        self.rect = self.image.get_rect()
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 60
        self.speed = speed



    def set_animation(self, animation_name):
        if animation_name in self.animations and animation_name != self.current_animation:
            self.current_animation = animation_name
            self.current_frame = 0



    def update(self):
        # Gérer les entrées de déplacement et l'inversion d'animation
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.set_animation("run")
            self.rect.x += self.speed
            self.Checkdirection("right")
        elif keys[pygame.K_LEFT]:
            self.set_animation("run")
            self.rect.x -= self.speed
            self.Checkdirection("left")
        else:
            self.set_animation("idle")

        # Mettre à jour la frame actuelle de l'animation
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.current_frame = (self.current_frame + 1) % len(self.animations[self.current_animation])
            self.image = self.animations[self.current_animation][self.current_frame]
            self.rect = self.image.get_rect(center=self.rect.center)

    def Checkdirection(self,direction):
        if direction=="left" and self.direction == "right":
                self.flip_images("left")
        if direction=="right" and self.direction == "left":
                self.flip_images("right")

    def flip_images(self, new_direction):
        """Inverse horizontalement les frames si le joueur change de direction."""
        self.direction = new_direction
        for anim_name, frames in self.animations.items():
            self.animations[anim_name] = [
                pygame.transform.flip(frame, True, False) for frame in frames
            ]