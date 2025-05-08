def poker_hands():
	"""
	Question: In the card game poker, a hand consists of five vards and are
	ranked, from lowest to highest, in the following way:
		High Card: Highest value card.
		One Pair: Two cards of the same value.
		Two Pair: Two different pairs.
		Three of a Kind: Three cards of the same value.
		Straight: All cards are consecutive values..
		Flush: All cards of the same suit.
		Full House: Three of a kind and a pair
		Four of a Kind: Four cards of the same value.
		Straight Flush: All cards are consecutive values of same unit.
		Royal Flush: Ten, Jack, Queen, King, Ace, in the same suit.
	The cards are valued in the order:
		2, 3, 4, 5, 6, 7, 8. 9, 10, Jack, Queen, King, Ace.
	If two players have the same ranked hands then the rank made up of the
	highest value wins; for example, a pair of eights beats a pair of fives (see
			example 1 below). But If two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.
	Consider the following five hands dealt to two players:
	Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
 	2C 3S 8S 8D TD
Pair of Eights
 	Player 2
2	 	5D 8C 9S JS AC
Highest card Ace
 	2C 5C 7D 8S QH
Highest card Queen
 	Player 1
3	 	2D 9C AS AH AC
Three Aces
 	3D 6D 7D TD QD
Flush with Diamonds
 	Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
 	3D 6D 7H QD QS
Pair of Queens
Highest card Seven
 	Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
 	3C 3D 3S 9S 9D
Full House
with Three Threes
 	Player 1
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
	"""
	count = 0
	with open('poker.txt', 'r') as f:
		for line in f:
			if player1_wins(line):
				count += 1
	return count



value_map = {'2': 2, '3': 3, '4': 4, '5': 5,
             '6': 6, '7': 7, '8': 8, '9': 9,
             'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

def parse_hand(cards):
	values = [value_map[c[0]] for c in cards]
	suits = [c[1] for c in cards]
	values.sort(reverse=True)

	# Manually count occurrences of each value
	counts = {}
	for v in values:
		counts[v] = counts.get(v, 0) + 1

	# Group values by frequency then sort (higher freq first, then higher value)
	freq_tuples = sorted(counts.items(), key=lambda x: (-x[1], -x[0]))
	freq_values = [v for v, count in freq_tuples]

	is_flush = all(s == suits[0] for s in suits)
	is_straight = len(set(values)) == 5 and max(values) - min(values) == 4

	if is_flush and is_straight:
		if max(values) == 14:
			return (9, values) # Royal flush
		return (8, values) # Straight flush
	elif freq_tuples[0][1] == 4:
		return (7, values) # Four of a kind
	elif freq_tuples[0][1] == 3 and freq_tuples[1][1] == 2:
		return (6, values) # Full house
	elif is_flush:
		return (5, values) # Flush
	elif is_straight:
		return (4, values) # Straight
	elif freq_tuples[0][1] == 3:
		return (3, freq_values) # Three of a kind
	elif freq_tuples[0][1] == 2 and freq_tuples[1][1] == 2:
		return (2, freq_values) # Two pairs
	elif freq_tuples[0][1] == 2:
		return (1, freq_values) # One pair
	else:
		return (0, values) # High card

def player1_wins(line):
	cards = line.strip().split()
	hand1 = parse_hand(cards[:5])
	hand2 = parse_hand(cards[5:])
	return hand1 > hand2


if __name__ == "__main__":
	print(poker_hands())
