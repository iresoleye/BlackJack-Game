class Card:

    def __init__(self,name,suit,rank):

        self.name = name
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.name


class Deck():

    suits = ['Hearts','Diamonds','Spades','Clubs']
    ranks = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']


    def __init__(self):
        self.deckofcards = []
        for x in Deck.suits:
            for y in Deck.ranks:

                if Deck.ranks.index(y)<9:
                    z = Card(y+" of "+x,x,Deck.ranks.index(y)+1)
                    self.deckofcards.append(z)

                else:
                    z = Card(y+" of "+x,x,10)
                    self.deckofcards.append(z)

        self.displayeddeckofcards = []
        for i in range(0,len(self.deckofcards)):
            self.displayeddeckofcards.append(self.deckofcards[i].name)
    

    def displayredo(self):
        self.displayeddeckofcards = []
        for i in range(0,len(self.deckofcards)):
            self.displayeddeckofcards.append(self.deckofcards[i].name)
        
    def shuffle(self):
        from random import shuffle
        shuffle(self.deckofcards)

    def collectrandomcard(self):
        from random import randint
        return self.deckofcards.pop(randint(0,len(self.deckofcards)-1))
        
            
    
