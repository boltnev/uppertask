import os
import sys
import time

import pygame
from trello import TrelloClient

import cfg

trello_client = TrelloClient(
    api_key=cfg.API_TOKEN,
    api_secret=cfg.API_TOKEN_SECRET,
    token=cfg.TOKEN,
)


RED = (255, 0, 0)
GREEN = (0, 255, 0)
FONT_HEIGHT = 36

pygame.init()

if cfg.FULLSCREEN:
    screen = pygame.display.set_mode((480,320), pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode((480,320))

screen.fill(GREEN)
pygame.mouse.set_visible(False)
pygame.display.update()

font = pygame.font.Font(cfg.FONT, 36)
font_color = (255,255,255)


class TrelloCommunicator:
    last_request_time = 0
    cached_label = ''

    def get_label(self):
        if time.time() - self.last_request_time < 10:
            return self.cached_label
        print("requesting trello")
        main_board = trello_client.get_board(cfg.BOARD)
        main_list = main_board.list_lists()[0]
        cards = main_list.list_cards()
        if cards:
            self.cached_label = str(cards[0].name)
        else:
            self.cached_label =  ''
        self.last_request_time = time.time()

        return self.cached_label

tc = TrelloCommunicator()

def update():
    label = tc.get_label()
    bgcolor = RED if label else GREEN

    lines = []
    line = []
    if label == '':
        label = cfg.ALL_DONE_MESSAGE
    
    for word in label.split():
        if sum([len(w) for w in line]) > 13:
            lines.append(' '.join(line))
            line = [word]
        else:
            line.append(word)
    lines.append(' '.join(line))

    screen.fill(bgcolor)
    for i, line in enumerate(lines):
        centery = 160 + FONT_HEIGHT * i - FONT_HEIGHT * (len(lines)-1) / 2
        t = font.render("{}".format(line), True, font_color, bgcolor)
        t_rect = t.get_rect()
    
        t_rect.centerx, t_rect.centery = 240, centery
        screen.blit(t, t_rect)
    


if __name__ == "__main__":
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        update()
        pygame.display.update()