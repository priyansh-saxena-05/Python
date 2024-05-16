import random

class SnakeAndLadder:
    def __init__(self, size=100):
        self.size = size
        self.board = [0] * (size + 1)  # Initialize board with default values (0)
        self.snakes = {}  # Dictionary to store snake positions
        self.ladders = {}  # Dictionary to store ladder positions

    def add_snake(self, start, end):
        self.snakes[start] = end

    def add_ladder(self, start, end):
        self.ladders[start] = end

    def roll_dice(self):
        return random.randint(1, 6)

    def move_player(self, player, steps):
        player.position += steps
        if player.position in self.snakes:
            player.position = self.snakes[player.position]
            print(f"Player {player.id} got bitten by a snake and moved to position {player.position}.")
        elif player.position in self.ladders:
            player.position = self.ladders[player.position]
            print(f"Player {player.id} climbed a ladder and moved to position {player.position}.")
        player.position = min(player.position, self.size)

    def play_game(self, players):
        while True:
            for player in players:
                steps = self.roll_dice()
                print(f"Player {player.id} rolled {steps}.")
                self.move_player(player, steps)
                print(f"Player {player.id} moved to position {player.position}.")
                if player.position == self.size:
                    print(f"Player {player.id} wins!")
                    return


class Player:
    def __init__(self, player_id):
        self.id = player_id
        self.position = 0  # Start position is 0 (not yet on the board)

# Example Usage:
game = SnakeAndLadder(size=100)
game.add_snake(99, 2)
game.add_snake(31, 12)
game.add_snake(16, 6)
game.add_ladder(45, 68)
game.add_ladder(4, 14)
game.add_ladder(2, 14)
players = [Player(1), Player(2)]

game.play_game(players)
