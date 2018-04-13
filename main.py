import player1;
import player2;

cards = ('5', '4', '3', '2', '1', '!')



# 1 == player1 win / 2 == player2 win / 0 == draw game
def winner_decision(player1_card, player2_card):

    if player1_card == '5':
        if player2_card == '5':
            return 0;
        elif player2_card == '2' or player2_card == '3' or player2_card == '4' or player2_card == '!':
            return 1;
        else:
            return 2;

    elif player1_card == '4':
        if player2_card == '4':
            return 0;
        elif player2_card == '2' or player2_card == '3' or player2_card == '1':
            return 1;
        else:
            return 2;

    elif player1_card == '3':
        if player2_card == '3':
            return 0;
        elif player2_card == '1' or player2_card == '2' or player2_card == '!':
            return 1;
        else:
            return 2;

    elif player1_card == '2':
        if player2_card == '2':
            return 0;
        elif player2_card == '1':
            return 1;
        else:
            return 2;

    elif player1_card == '1':
        if player2_card == '1':
            return 0;
        elif player2_card == '!' or player2_card == '5':
            return 1;
        else:
            return 2;

    elif player1_card == '!':
        if player2_card == '!':
            return 0;
        elif player2_card == '2' or player2_card == '4':
            return 1;
        else:
            return 2;


class stateOfPlay:
    def __init__(self):
        self.p1_old_games = []
        self.p2_old_games = []

        self.p1_game_score = 0
        self.p2_game_score = 0

        self.match_count = 0
        self.p1_win_count = 0
        self.p2_win_count = 0

        self.match_final_result = 0

        self.isGameOver = False

    def update_old_games(self, p1_history, p2_history):
        self.p1_old_games.append(p1_history)
        self.p2_old_games.append(p2_history)

    def update_match_result(self, result):
        if result == 1:
            self.p1_game_score += 3
            self.p1_win_count += 1
        elif result == 2:
            self.p2_game_score += 3
            self.p2_win_count += 1
        else:
            self.p1_game_score += 1
            self.p2_game_score += 1

        print("최종점수 => P1:" + str(self.p1_game_score) + "  P2:" + str(self.p2_game_score))


    def checkIsGameOver(self):
        if self.p1_win_count >= 6:
            self.match_final_result = 1
            self.isGameOver = True
        elif self.p2_win_count >= 6:
            self.match_final_result = 2
            self.isGameOver = True
        elif self.match_count >= 10:
            self.isGameOver = True
            if self.p1_game_score > self.p2_game_score:
                self.match_final_result = 1
            elif self.p2_game_score > self.p1_game_score:
                self.match_final_result = 2
            else:
                return 0


class eachGame:
    def __init__(self):
        self.p1_history = []
        self.p2_history = []
        self.p1_hand = ['1', '2', '3', '4', '5', '!']
        self.p2_hand = ['1', '2', '3', '4', '5', '!']
        self.p1_score = 0
        self.p2_score = 0

        self.turn = 0

        self.isEndGame = False

        self.winnerOfThisGame = 0

    def nextGame(self, p1_old_games, p2_old_games):

        p1_decision = player1.think(self.p1_hand, self.p1_history, p1_old_games)
        p2_decision = player2.think(self.p2_hand, self.p2_history, p2_old_games)

        self.p1_history.append([p1_decision, p2_decision])
        self.p2_history.append([p2_decision, p1_decision])

        print('히스토리: ' + str(self.p1_history))
        print('점수: P1:' + str(self.p1_score) + " P2:" + str(self.p2_score))

        self.p1_hand.remove(p1_decision)
        self.p2_hand.remove(p2_decision)

        winner = winner_decision(p1_decision, p2_decision)

        if winner == 1:
            self.p1_score += 1
            self.p2_score -= 1
        elif winner == 2:
            self.p1_score -= 1
            self.p2_score += 1

        self.turn += 1

        if self.p1_score >= 3:
            self.winnerOfThisGame = 1
            self.isEndGame = True
        elif self.p2_score >= 3:
            self.winnerOfThisGame = 2
            self.isEndGame = True
        elif self.p1_score <= -3:
            self.winnerOfThisGame = 2
            self.isEndGame = True
        elif self.p2_score <= -3:
            self.winnerOfThisGame = 1
            self.isEndGame = True

        # If finish the last turn, have to decide the winner
        if self.turn >= 6:
            self.isEndGame = True
            if self.p1_score > self.p2_score:
                self.winnerOfThisGame = 1
            elif self.p1_score < self.p2_score:
                self.winnerOfThisGame = 2
            else:
                self.winnerOfThisGame = 0

    def getHistories(self):
            return [self.p1_history, self.p2_history]


# Main game
mainGameStatus = stateOfPlay()

while not mainGameStatus.isGameOver:

    game = eachGame()

    print('<<' + str(mainGameStatus.match_count + 1) + '번째 매치>>')

    while not game.isEndGame:
        game.nextGame(mainGameStatus.p1_old_games, mainGameStatus.p2_old_games)

        if game.isEndGame:
            histories = game.getHistories()
            mainGameStatus.update_old_games(histories[0], histories[1])
            mainGameStatus.update_match_result(game.winnerOfThisGame)

    mainGameStatus.checkIsGameOver()

    mainGameStatus.match_count += 1

