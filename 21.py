import random
from os import system, name
weight_cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 2, 'Q': 3, 'K': 4, 'A': 11}
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
cards_in_hand = []
cards_in_diller = []
sum_hand = 0
sum_hand_diller = 0
while True:
    reserv = random.choice(cards)
    cards_in_hand.append(reserv)
    for i in range(len(cards_in_hand)):
        print(cards_in_hand[i])
    sum_hand =sum([weight_cards[x] for x in cards_in_hand])
    print(sum([weight_cards[x] for x in cards_in_hand]))
    if sum_hand > 21:
        print(f"Перебор на {sum_hand-21} \nПереход хода")
        break
    choice=input("Ещё? Y/N")
    if choice == 'Y' or choice == 'y':
        continue
    else:
        print("Переход хода")

        break
while True:
    reserv = random.choice(cards)
    cards_in_diller.append(reserv)
    for i in range(len(cards_in_diller)):
        print(cards_in_diller[i])
    sum_hand_diller = sum([weight_cards[x] for x in cards_in_diller])
    print(sum([weight_cards[x] for x in cards_in_diller]))
    if sum_hand_diller > 21:
        print(f"Перебор на {sum_hand_diller-21}\nПереход хода")

        break
    choice = input("Ещё? Y/N")
    if choice == 'Y' or choice == 'y':
        continue
    else:

        break
print("Результаты")
print(f"Игрок {sum_hand}")
print(f"Диллер {sum_hand_diller}")
while True:
    if sum_hand>21 and sum_hand_diller <= 21:
        print("Выиграл Диллер")
        break
    if sum_hand_diller>21 and sum_hand<=21:
        print("Выиграл Игрок")
        break
    if sum_hand > 21 and sum_hand_diller > 21:
         if sum_hand < sum_hand_diller:
             print("Выиграл Игрок")
             break
         else:
            print("Выиграл Диллер")
            break
    if sum_hand>sum_hand_diller:
        print("Выиграл Игрок")
        break
    if sum_hand_diller>sum_hand:
        print("Выиграл Диллер")
        break
    if sum_hand==sum_hand_diller:
        print("Ничья")
        break