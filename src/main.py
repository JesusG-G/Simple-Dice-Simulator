import random
import keyboard as keyboard

def roll_dice(amount_of_dices: int, number_dice_faces: int = 6) -> list[int]:
    if amount_of_dices <= 0 or number_dice_faces < 2:
        raise ValueError
    
    dices: list[int] = []
    for _ in range(amount_of_dices):
        random_roll: int = random.randint(1,number_dice_faces)
        dices.append(random_roll)
    return dices



def main():
    while True:
        try:
            number_dice_faces: str = input("How many faceses do you want the dice have?: ")
            if not number_dice_faces.isnumeric():
                raise ValueError
            amount_of_dices: str = input("How many dices do you want to roll?: ")
            if not amount_of_dices.isnumeric():
                raise ValueError
            result = roll_dice(int(amount_of_dices), int(number_dice_faces))
            print(*result, sep=', ')
        except ValueError:
            print("Please introduce a valid number")

if __name__ == "__main__":
    main()