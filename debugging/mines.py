#!/usr/bin/env python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.total_cells = width * height
        self.mine_count = mines

        # Store mines as (x, y) tuples instead of flat indices
        all_cells = [(x, y) for x in range(width) for y in range(height)]
        self.mines = set(random.sample(all_cells, mines))

        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('   ' + ' '.join(f"{i:2}" for i in range(self.width)))
        for y in range(self.height):
            print(f"{y:2} ", end='')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (x, y) in self.mines:
                        print(' *', end='')
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(f" {count}" if count > 0 else "  ", end='')
                else:
                    print(' .', end='')
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if (dx == 0 and dy == 0):
                    continue
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (nx, ny) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            return True  # Ignore invalid coords without crashing

        if self.revealed[y][x]:
            return True  # Already revealed

        if (x, y) in self.mines:
            return False

        self.revealed[y][x] = True

        if self.count_mines_nearby(x, y) == 0:
            # Reveal neighbors recursively
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if (dx != 0 or dy != 0):
                        self.reveal(nx, ny)
        return True

    def is_won(self):
        revealed_count = sum(row.count(True) for row in self.revealed)
        return revealed_count == self.total_cells - self.mine_count

    def play(self):
        while True:
            self.print_board()
            try:
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                if not (0 <= x < self.width and 0 <= y < self.height):
                    print("Coordinates out of bounds.")
                    input("Press Enter to continue...")
                    continue

                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("\n💥 Game Over! You hit a mine.")
                    break

                if self.is_won():
                    self.print_board(reveal=True)
                    print("\n🎉 Congratulations! You cleared the field!")
                    break

            except ValueError:
                print("Invalid input. Please enter numbers only.")
                input("Press Enter to continue...")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()
