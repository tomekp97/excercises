import sys
import random

import pygame

pygame.init()

WIDTH = 500
HEIGHT = 500
SCREEN_AREA = WIDTH * HEIGHT
TILE_DIMENSIONS = 10
TILE_OFFSET = 10
TILE_AREA = TILE_DIMENSIONS**2
tiles_lost_out_of_bounds = 0

GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class Tile(pygame.Rect):
    def __init__(self, x, y, width, height):
        pygame.Rect.__init__(self, x, y, width, height)

        self.colour = (GREEN)
        self.is_spawned = False
        self.random_number = random.randrange(0, 100)
        self.spawn_chance = 90

    def spawn(self):
        self.x = random.randrange(1, (200 - self.width))
        self.y = random.randrange(1, (200 - self.height))
    
    def move_to_side_of_neighbour(self, tiles_list, neighbour_index):
        """ Need to get the difference between self.x and neighbour.x"""
        collision_x = self.x
        collision_y = self.y

        neighbour_tile = tiles_list[neighbour_index]
        neighbour_x = neighbour_tile.x
        neighbour_y = neighbour_tile.y
        neighbour_width = neighbour_tile.width
        neighbour_height = neighbour_tile.height

        difference_x = collision_x - neighbour_x
        difference_y = collision_y - neighbour_y

        # print("Difference X: " + str(difference_x) + "\nDifference Y: " + str(difference_y) + "\n")

        if (difference_x >= 0):
            self.x = int(neighbour_tile.right)
        else:
            self.x = int(neighbour_tile.left - self.width)

        if (difference_y >= 0):
            self.y = int(neighbour_tile.bottom)
        else:
            self.y = int(neighbour_tile.top - self.height)
        
        self.check_collision_with_neighbour(tiles_list)

        if self.right > WIDTH or self.left < 0 or self.bottom > HEIGHT or self.top < 0:
            self.x = -100
            self.y = -100

    def check_collision_with_neighbour(self, tiles_list):
        # print(self)
        try:
            neighbour_index = self.collidelist(tiles_list)
            if neighbour_index > -1:
                self.move_to_side_of_neighbour(tiles_list, neighbour_index)
            
            print(tile)
        except:
            print("\n=== Failed here: ===")
            print(self)
            print("====================\n")


            
    # def check_if_colliding_after_shifting(self, tiles_list, neighbour_index):
    #     neighbour_index = self.collidelist(tiles_list)
    #     if neighbour_index < 0:
    #         return False

    #     self.move_to_side_of_neighbour(tiles_list, neighbour_index)
        

    def will_spawn(self):
        return True if self.random_number <= self.spawn_chance else False


def prepare_map():
    # iterations = int(SCREEN_AREA / TILE_AREA)
    iterations = 100
    tiles = []
    spawned_tiles = 0

    """ Here I will check if the Tile() .will_spawn(), if so, run .spawned()
    to generate coords and add it to the tiles[] array """
    for pixel in range(iterations):
        tile = Tile(0, 0, TILE_DIMENSIONS, TILE_DIMENSIONS)
        
        if tile.will_spawn():
            tile.spawn()

            """ Get previous tile from array """
            if tiles:
                """ If current tile overlaps previous_tile, move current tile """
                tile.check_collision_with_neighbour(tiles)
            
                # neighbour_index = tile.check_collision_with_neighbour(tiles)
                # if neighbour_index > -1:
                #     tile.move_to_side_of_neighbour(tiles, neighbour_index, tiles_lost_out_of_bounds)
            # print(tile)
            # break
            tiles.append(tile)
            del tile

            spawned_tiles += 1
    tiles_after_potential_removal = len(tiles)

    print("Iterations: " + str(iterations))
    print("Tiles initially spawned: " + str(spawned_tiles))
    print("Tiles actually on screen: " + str(tiles_after_potential_removal))
    print("Tiles lost out of bounds: " + str(tiles_lost_out_of_bounds))
    return tiles

def draw_map():
    tiles = prepare_map()

    for tile in tiles:
        pygame.draw.rect(screen, tile.colour, tile)

screen.fill(BLUE)
draw_map()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()



    pygame.display.update()