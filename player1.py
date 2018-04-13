def think(hands, history, old_games):

    if len(history) != 0:
        enemy_hands = enemy_deck_count(history)
        #print(enemy_hands)
        select_weight = calculate_win_percent(hands, enemy_hands)
        #print(select_weight)

        return select_card(select_weight)
    else:
        return '2'


def enemy_deck_count(prev_history):
    card_deck = ['1', '2', '3', '4', '5', '!']

    for hist in prev_history:
        if hist[1] in card_deck:
            card_deck.remove(hist[1])

    return card_deck


def calculate_win_percent(my_hands, enemy_hands):
    select_weight = {}

    for my_card in my_hands:

        if my_card is '1':
            select_weight[my_card] = 0
            for enemy_card in enemy_hands:
                if enemy_card is '5' or enemy_card is '!':
                    select_weight[my_card] = select_weight[my_card] + 1
                else:
                    select_weight[my_card] = select_weight[my_card] - 1

        elif my_card is '2':
            select_weight[my_card] = 0
            for enemy_card in enemy_hands:
                if enemy_card is '1':
                    select_weight[my_card] = select_weight[my_card] + 1
                else:
                    select_weight[my_card] = select_weight[my_card] - 1

        elif my_card is '3':
            select_weight[my_card] = 0
            for enemy_card in enemy_hands:
                if enemy_card is '1' or enemy_card is '2' or enemy_card is '!':
                    select_weight[my_card] = select_weight[my_card] + 1
                else:
                    select_weight[my_card] = select_weight[my_card] - 1

        elif my_card is '4':
            select_weight[my_card] = 0
            for enemy_card in enemy_hands:
                if enemy_card is '1' or enemy_card is '2' or enemy_card is '3':
                    select_weight[my_card] = select_weight[my_card] + 1
                else:
                    select_weight[my_card] = select_weight[my_card] - 1

        elif my_card is '5':
            select_weight[my_card] = 0
            for enemy_card in enemy_hands:
                if enemy_card is '2' or enemy_card is '3' or enemy_card is '4' or enemy_card is '!':
                    select_weight[my_card] = select_weight[my_card] + 1
                else:
                    select_weight[my_card] = select_weight[my_card] - 1

        elif my_card is '!':
            select_weight[my_card] = 0
            for enemy_card in enemy_hands:
                if enemy_card is '2' or enemy_card is '4':
                    select_weight[my_card] = select_weight[my_card] + 1
                else:
                    select_weight[my_card] = select_weight[my_card] - 1

    return select_weight

def select_card(select_weight):
    select_card = max(select_weight, key=select_weight.get)

    return select_card