k=int(input("Введите количество карт"))
current_hand = []
cards = {"2": 1, "3": 1, "4": 1, "5": 1, "6": 1, "7": 0, "8": 0, "9": 0, "10": -1, "J": -1, "Q": -1, "K": -1, "A": -1}
for i in range(k):
    cards_in_hand=input()
    current_hand.append(cards_in_hand)
cards_sum=sum([cards[x] for x in current_hand])
print(cards_sum)