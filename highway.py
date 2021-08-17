#!/usr/bin/env python3

import sys
import os
import argparse
from pathlib import Path

import pygame

class Application():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("HighwayBingo")
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        i = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    key = pygame.key.name(event.key)
                    if key == 'escape':
                        running = False
            i = (i + 1) % 256
            self.screen.fill((i, i, i))
            pygame.display.update()
            self.clock.tick(60)


def get_images(image_dir):
    imageExtensions = ['.png', '.jpg']
    images = list()
    for item in os.listdir(image_dir):
        if os.path.isfile(os.path.join(image_dir, item)) and \
                (str(Path(item).suffix) in imageExtensions):
            images.append(item)
    return images


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
    description=('HighwayBingo creates image sheets for "I spy with my little '
        'eye..."-bingo-like games on long car trips.'))

    parser.add_argument(
        'image_directory',
        metavar='images',
        nargs='?',
        default=os.path.join(str(Path(__file__).parent), 'images'),
        help='Parent directory of the images used for the bingo field.')

    parser.add_argument(
        '-s', '--size',
        nargs='?',
        default=4,
        help='Number of rows and columns.')

    args = parser.parse_args()

    images = get_images(args.image_directory)

    app = Application()
    app.run()
    sys.exit(0)

