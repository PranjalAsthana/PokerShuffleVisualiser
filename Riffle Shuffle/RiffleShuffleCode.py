deck = [*range(1,53)] # deck of 52 cards
for i in range(n): # declare no of shuffles
    mid = len(deck)//2 # assuming perfect middle split
    deck1 = deck[:mid]
    deck2 = deck[mid:]
    deck = []
    #print(deck1,deck2)
    for i in range(mid):
        deck.append(deck1[i])
        deck.append(deck2[i])
    print(deck)
