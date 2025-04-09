import pygame
import random
grid_size = 100
cell_size = 5
width, height = grid_size * cell_size, grid_size * cell_size
fps = 30
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
class Ant:
    def __init__(self, x, y, color, pheromone):
        self.x = x
        self.y = y
        self.direction = 0
        self.color = color
        self.pheromone = pheromone
    def move(self, grid):
        current_state = grid[self.y][self.x]
        current_pheromone = pheromones[self.y][self.x]
        if current_pheromone == self.pheromone:
            if random.random() < 0.8:
                self.x = (self.x + directions[self.direction][0]) % grid_size
                self.y = (self.y + directions[self.direction][1]) % grid_size
                return
        elif current_pheromone is not None:
            if random.random() >= 0.8:
                self.x = (self.x + directions[self.direction][0]) % grid_size
                self.y = (self.y + directions[self.direction][1]) % grid_size
                return
        if current_state == 0:
            self.direction = (self.direction + 1) % 4
        else:
            self.direction = (self.direction - 1) % 4
        grid[self.y][self.x] = 1 - grid[self.y][self.x]
        pheromones[self.y][self.x] = self.pheromone
        decay_timers[self.y][self.x] = 5
        self.x = (self.x + directions[self.direction][0]) % grid_size
        self.y = (self.y + directions[self.direction][1]) % grid_size
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
pheromones = [[None for _ in range(grid_size)] for _ in range(grid_size)]
decay_timers = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
ant1 = Ant(grid_size//3, grid_size//2, (255, 0, 0), 'A')
ant2 = Ant(2*grid_size//3, grid_size//2, (0, 0, 255), 'B')
ants = [ant1, ant2]
running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for ant in ants:
        ant.move(grid)
    for y in range(grid_size):
        for x in range(grid_size):
            if decay_timers[y][x] > 0:
                decay_timers[y][x] -= 1
                if decay_timers[y][x] == 0:
                    pheromones[y][x] = None
    for y in range(grid_size):
        for x in range(grid_size):
            color = (255, 255, 255) if grid[y][x] == 0 else (0, 0, 0)
            pygame.draw.rect(screen, color, (x*cell_size, y*cell_size, cell_size, cell_size))
            if pheromones[y][x] == 'A':
                pygame.draw.circle(screen, (255, 200, 200), (x*cell_size + cell_size//2, y*cell_size + cell_size//2), 2)
            elif pheromones[y][x] == 'B':
                pygame.draw.circle(screen, (200, 200, 255), (x*cell_size + cell_size//2, y*cell_size + cell_size//2), 2)
    for ant in ants:
        pygame.draw.rect(screen, ant.color, (ant.x * cell_size, ant.y * cell_size, cell_size, cell_size))
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()