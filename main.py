import pygame
import sys
import players,spritesheet

class Game:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("test pia")
        self.clock = pygame.time.Clock()
        self.running = True
        self.bg_color = (40, 44, 52)
        self.load_assets()
        self.player = players.Player(self.sprite_sheet,speed=1.5)
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

    def load_assets(self):
        COL_KEY = (232, 160, 255)
        self.sprite_sheet = spritesheet.SpriteSheet("Assets/images/kirby.png", COL_KEY)
        self.sprite_sheet.add_animation("idle", [(0, 9, 41, 53)],scale=2)
        self.sprite_sheet.add_animation("run", [(11, 112, 25, 38), (40, 113, 28, 37), (72, 113, 31, 37),(107,113,32,37),(144,113,32,37),(180,112,28,38),(212,111,24,39)],scale=2)

    def run(self):
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.draw()

        self.quit_game()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def update(self):
        self.player.update()
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(self.bg_color)
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def quit_game(self):
        pygame.quit()
        sys.exit()

Game(800,800).run()