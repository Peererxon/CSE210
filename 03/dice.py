from random import randint


class Dice:
    def __init__(self):
        self.number = 0

    def rol(self):
        self.number = randint(0, 5)


class Player:
    def __init__(selft, name):
        selft.name = name


class Game:
    def __init__(self, player: Player):
        self.point = 0
        self.player = player
        self.is_over = False
        self.rolled_list = []

    def rol_dices(self):
        for _ in range(5):
            dice = Dice()
            dice.rol()
            rolled_number = dice.number
            self.rolled_list.append(rolled_number)

    def show_dices(self):
        print('Your rolled: ', *self.rolled_list)

    def show_score(self):
        print(f'Your score is: {self.point}')

    def check_dices(self):
        is_valid = False  # the rolled will be valid if at least one of the number is 5 or 1
        for dice_number in self.rolled_list:
            if dice_number == 5:
                self.point += 50
                is_valid = True
            elif dice_number == 1:
                self.point += 100
                is_valid = True
        self.is_over = True if (is_valid == False) else False

    def start_game(self):
        while not self.is_over:
            player_answer = input('Roll Dice? [y/n]: ')
            self.is_over = False if player_answer == 'y' else True
            if self.is_over:
                break
            self.rol_dices()
            self.show_dices()
            self.check_dices()
            self.show_score()
            self.end_turn()
            print()

    def end_turn(self):
        self.rolled_list = []

    def end_game(self):
        print(f'{self.player.name} Thanks for playing!')
        print(f'You scored a total score of: {self.point}!')


def main():
    player = Player('Anderson')
    game = Game(player)
    game.start_game()
    game.end_game()


main()
