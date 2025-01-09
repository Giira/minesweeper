from main import DIFFICULTY
from random import randint

difficulties = {
    "Easy": [(9, 9), 10],
    "Medium": [(16, 16), 40],
    "Hard": [(30, 16), 99],
}


class Grid:
    def __init__(self):
        self.grid_width = difficulties[DIFFICULTY][0][0]
        self.grid_height = difficulties[DIFFICULTY][0][1]
        self.mine_total = difficulties[DIFFICULTY][1]
        self.mine_coords = set()
        self.button_grid = []

        for i in range(self.grid_height):
            self.button_grid.append([])
            for j in range(self.grid_width):
                self.button_grid[i].append(Cell(i, j, self))
        
        self.place_mines()

        for i in range(self.grid_height):
            for j in range(self.grid_width):
                self.button_grid[i][j].find_neighbours()
                self.button_grid[i][j].get_score()
    

    def place_mines(self):
        while len(self.mine_coords) < self.mine_total:
            self.mine_coords.add((randint(0, self.grid_height - 1), randint(0, self.grid_width - 1)))
        for coord in sorted(self.mine_coords):
            self.button_grid[coord[0]][coord[1]].mine = True
    

class Cell:
    def __init__(self, x, y, Grid):
        self.x = x
        self.y = y
        self.mine = False
        self.neighbours = []
        self.score = 0
    

    def find_neighbours(self):
        if self.x > 0:
            self.neighbours.append((self.x -1, self.y))
        if self.y > 0:
            self.neighbours.append((self.x, self.y -1))
        if self.x < Grid.grid_height:
            self.neighbours.append((self.x +1, self.y))
        if self.y < Grid.grid_width:
            self.neighbours.append((self.x, self.y +1))


    def get_score(self):
        for neighbour in self.neighbours:
            if neighbour.mine:
                self.score += 1
