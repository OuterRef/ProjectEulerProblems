# <p>In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:</p>
# <ul><li><b>High Card</b>: Highest value card.</li>
# <li><b>One Pair</b>: Two cards of the same value.</li>
# <li><b>Two Pairs</b>: Two different pairs.</li>
# <li><b>Three of a Kind</b>: Three cards of the same value.</li>
# <li><b>Straight</b>: All cards are consecutive values.</li>
# <li><b>Flush</b>: All cards of the same suit.</li>
# <li><b>Full House</b>: Three of a kind and a pair.</li>
# <li><b>Four of a Kind</b>: Four cards of the same value.</li>
# <li><b>Straight Flush</b>: All cards are consecutive values of same suit.</li>
# <li><b>Royal Flush</b>: Ten, Jack, Queen, King, Ace, in same suit.</li>
# </ul><p>The cards are valued in the order:<br>2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.</p>
# <p>If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.</p>
# <p>Consider the following five hands dealt to two players:</p>
# <div class="center">
# <table><tr><td><b>Hand</b></td><td> </td><td><b>Player 1</b></td><td> </td><td><b>Player 2</b></td><td> </td><td><b>Winner</b></td>
# </tr><tr><td><b>1</b></td><td> </td><td>5H 5C 6S 7S KD<br><div class="smaller">Pair of Fives</div></td><td> </td><td>2C 3S 8S 8D TD<br><div class="smaller">Pair of Eights</div></td><td> </td><td>Player 2</td>
# </tr><tr><td><b>2</b></td><td> </td><td>5D 8C 9S JS AC<br><div class="smaller">Highest card Ace</div></td><td> </td><td>2C 5C 7D 8S QH<br><div class="smaller">Highest card Queen</div></td><td> </td><td>Player 1</td>
# </tr><tr><td><b>3</b></td><td> </td><td>2D 9C AS AH AC<br><div class="smaller">Three Aces</div></td><td> </td><td>3D 6D 7D TD QD<br><div class="smaller">Flush  with Diamonds</div></td><td> </td><td>Player 2</td>
# </tr><tr><td><b>4</b></td><td> </td><td>4D 6S 9H QH QC<br><div class="smaller">Pair of Queens<br>Highest card Nine</div></td><td> </td><td>3D 6D 7H QD QS<br><div class="smaller">Pair of Queens<br>Highest card Seven</div></td><td> </td><td>Player 1</td>
# </tr><tr><td><b>5</b></td><td> </td><td>2H 2D 4C 4D 4S<br><div class="smaller">Full House<br>With Three Fours</div></td><td> </td><td>3C 3D 3S 9S 9D<br><div class="smaller">Full House<br>with Three Threes</div></td><td> </td><td>Player 1</td>
# </tr></table></div>
# <p>The file, <a href="resources/documents/0054_poker.txt">poker.txt</a>, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.</p>
# <p>How many hands does Player 1 win?</p>

from typing import List, Dict
import time

TIE = 0
HIGH_CARD = 1
ONE_PAIR  = 2
TWO_PAIRS = 3
THREE_OF_A_KIND = 4
STRAIGHT = 5
FLUSH = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
STRAIGHT_FLUSH = 9
ROYAL_FLUSH = 10

# tie_breaker = {
#     # Tied rank: next rank to eval
#     # TIE means tied
#     HIGH_CARD: HIGH_CARD,
#     ONE_PAIR: HIGH_CARD,
#     TWO_PAIRS: ONE_PAIR,
#     THREE_OF_A_KIND: HIGH_CARD,
#     STRAIGHT: TIE,
#     FLUSH: HIGH_CARD,
#     FULL_HOUSE: ONE_PAIR,
#     FOUR_OF_A_KIND: HIGH_CARD,
#     STRAIGHT_FLUSH: TIE,
#     ROYAL_FLUSH: TIE
# }

def elem_count(value_list: List[str]) -> Dict[str, List[int]]:
    count_dict = {}
    for idx in range(len(value_list)):
        if value_list[idx] in count_dict:
            count_dict[value_list[idx]].append(idx)
        else:
            count_dict[value_list[idx]] = [idx]
    return count_dict

class Cards():
    
    def __init__(self, card_str: str):
        self.cards = card_str.split()
        self.value_map = {
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            'T': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14,
        }
        self.values = [self.value_map[s[0]] for s in self.cards]
        self.suits  = [s[1] for s in self.cards]
        self.rank = TIE
        self.compare_seq = []
        self.rank = self.find_rank()
    
    def find_rank(self):
        # find max repeated number
        # None, 1, 2, 3, 4
        repeat_flags = [None, 0, 0, 0, 0]
        repeat_values = [None, [], [], [], []]
        count_dict = elem_count(self.values)
        for k, v in count_dict.items():
            repeat_flags[len(v)] += 1
            repeat_values[len(v)].append(k)
        ## 4 -> four of a kind
        if repeat_flags[4]:
            self.compare_seq.append(repeat_values[4][0])
            self.compare_seq.append(repeat_values[1][0])
            return FOUR_OF_A_KIND
        ## 3 -> full house / three of a kind
        if repeat_flags[3]:
            self.compare_seq.append(repeat_values[3][0])
            if repeat_flags[2]:
                self.compare_seq.append(repeat_values[2][0])
                return FULL_HOUSE
            else:
                repeat_values[1].sort(reverse=True)
                self.compare_seq.extend(repeat_values[1])
                return THREE_OF_A_KIND
        ## 2 -> two pairs / one pair
        if repeat_flags[2]:
            self.compare_seq.append(max(repeat_values[2]))
            if repeat_flags[2] == 2:
                self.compare_seq.append(min(repeat_values[2]))
                self.compare_seq.append(repeat_values[1][0])
                return TWO_PAIRS
            else:
                repeat_values[1].sort(reverse=True)
                self.compare_seq.extend(repeat_values[1])
                return ONE_PAIR

        # no repeated number
        if max(self.values) - min(self.values) == 4:
            ## is straight
            self.compare_seq.append(max(self.values))
            if len(set(self.suits)) == 1:
                ### is straight flush
                if max(self.values) == 14:
                    #### is royal flush
                    return ROYAL_FLUSH
                return STRAIGHT_FLUSH
            return STRAIGHT

        ## is flush
        if len(set(self.suits)) == 1:
            self.compare_seq.append(max(self.values))
            return FLUSH

        repeat_values[1].sort(reverse=True)
        self.compare_seq.extend(repeat_values[1])
        return HIGH_CARD


def winner(line: str):
    p1_cards = Cards(line[:14])
    p2_cards = Cards(line[15:])
    if p1_cards.rank > p2_cards.rank:
        return "p1"
    elif p2_cards.rank > p1_cards.rank:
        return "p2"
    else:
        if p1_cards.compare_seq > p2_cards.compare_seq:
            return "p1"
        elif p1_cards.compare_seq < p2_cards.compare_seq:
            return "p2"
        else:
            return "tie"

if __name__ == "__main__":
    start = time.time()
    with open("./files/problem54_file.txt", "r") as f:
        lines = f.readlines()

    p1_win = 0
    for line in lines:
        if winner(line) == 'p1':
            p1_win += 1
    end = time.time()
    print(p1_win)
    print(end - start)

    # print(winner("3D KH QD 6C 6S AD AS 8H 2H QS"))
    # print(winner("3D 6H 6D 6C 6S AD AS AH 2H 2S"))
    # print(winner("3D KH 6D 6C 6S AD AS KH 2H 2S"))
    # print(winner("3D 4H 5D 6C 6S TD JS QH KH AS"))
    # print(winner("3D 4H 5D 6C 9S TD JD QD KD AD"))
    # print(winner("3S 4S 5S 6S 7S 6D JD QD KD AD"))
    # print(winner("TS JS QS KS AS TD JD QD KD AD"))
