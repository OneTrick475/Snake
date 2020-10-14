import pygame
from random import randrange
pygame.font.init()


class Snake:
    body = [[250, 250], [250, 260], [250, 270]]

    def has_lost(self):
        if self.body[0] in self.body[1:]:
            return True
        if self.body[0][0] < 0 or self.body[0][0] > 500 or self.body[0][1] < 0 or self.body[0][1] > 500:
            return True
        return False

    def draw(self, win, apple):
        win.fill((0, 0, 0))
        pygame.draw.rect(win, (255, 0, 0), (apple[0], apple[1], 10, 10))
        for head in self.body:
            pygame.draw.rect(win, (255, 255, 255),
                             (head[0], head[1], 9, 9))

    def move(self, key):
        pygame.time.delay(100)
        head = self.body[0]
        prev = list(head)

        if key == 'UP':
            head[1] -= 10
        if key == 'DOWN':
            head[1] += 10
        if key == 'RIGHT':
            head[0] += 10
        if key == 'LEFT':
            head[0] -= 10

        for i in range(1, len(self.body)):
            prev2 = self.body[i]
            self.body[i] = prev
            prev = prev2

    def spawn_apple(self):
        return [randrange(0, 500, 10), randrange(0, 500, 10)]

    def has_eat(self, apple):
        if self.body[0] == apple:
            return True
        return False

    def draw_lost(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)
        text = fnt.render('You have lost', 10, (255, 255, 255))

        win.blit(text, (150, 200))
        pygame.display.update()

    def play(self):
        win = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Snake")
        run = True
        key = 'UP'
        apple = self.spawn_apple()

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        key = 'UP' if key != 'DOWN' else 'DOWN'
                    if event.key == pygame.K_DOWN:
                        key = 'DOWN' if key != 'UP' else 'UP'
                    if event.key == pygame.K_RIGHT:
                        key = 'RIGHT' if key != 'LEFT' else 'LEFT'
                    if event.key == pygame.K_LEFT:
                        key = 'LEFT' if key != 'RIGHT' else 'RIGHT'

            if self.has_lost():
                self.draw_lost(win)
                pygame.event.clear()
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            return
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                self.body = [[250, 250], [
                                    250, 260], [250, 270]]
                                self.play()

            self.move(key)

            if self.has_eat(apple):
                last = list(self.body[-1])
                if key == 'UP':
                    last[1] -= 10
                if key == 'DOWN':
                    last[1] += 10
                if key == 'RIGHT':
                    last[0] += 10
                if key == 'LEFT':
                    last[0] -= 10
                self.body.append(last)
                apple = self.spawn_apple()

            self.draw(win, apple)
            pygame.display.update()


idk = Snake()
idk.play()
