
cards = ('5', '4', '3', '2', '1', '!')

def think(hands, history, old_games):
    if len(history) == 0:
        return '5'
    if len(history) == 1:
        return '4'
    if len(history) == 2:
        return '3'
    if len(history) == 3:
        return '2'
    if len(history) == 4:
        return '1'
    if len(history) == 5:
        return '!'