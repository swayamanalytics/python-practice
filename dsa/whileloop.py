from functools import partial
import random

class Card(object):
    def __init__(self,rank,suit):
        self.suit=suit
        self.rank=rank
        self.hardPoint,self.softPoint=self._points()

class FaceCard(Card):
    def _points(self):
        return 10,10

class AceCard(Card):
    def _points(self):
        return 1,11


class NumberCard(Card):
    def _points(self):
        return self.rank,self.rank


class Suit(object):
    def __init__(self,name,symbol):
        self.name=name
        self.symbol=symbol

class CardGenerator(object):
    def rank(self,rank):
        self.class_,self.rankStr={1:(AceCard,'A'),11:(FaceCard,'J'),12:(FaceCard,'Q'),13:(FaceCard,'K')}.get(rank,(NumberCard,str(rank)))
        return self

    def suit(self,suit):
        return self.class_(self.rankStr,suit)
    


class Deck:
    def __init__(self):
        club, diamond, heart, spade = Suit('Club', '♣'), Suit('Diamond', '♦'), Suit('Heart', '♥'), Suit('Spade', '♠')
        cardd=CardGenerator()
        self._cards=[cardd.rank(i).suit(j) for i in range(1,14) for j in [club, diamond, heart, spade]]
        random.shuffle(self._cards)

    def pop(self):
        return self._cards.pop()


     

def card(rank,suit):
    if 1< rank <11:
        return NumberCard(suit,str(rank))
    elif  14 > rank > 10:
        name={ 11:'J',12:'Q',13:'K'}[rank]
        return FaceCard(suit,name)
    elif rank == 1:
        return AceCard(suit,str(rank))
    else:
        raise Exception("Not Found a Card")


def card2(rank,suit):
    class_={1:AceCard,11:FaceCard,12:FaceCard,13:FaceCard}.get(rank,NumberCard)
    rankStr={1:'A',11:'J',12:'Q',13:'K'}.get(rank,str(rank))
    return class_(rankStr,suit)


class Deck1(list):
    def __init__(self):
        club, diamond, heart, spade = Suit('Club', '♣'), Suit('Diamond', '♦'), Suit('Heart', '♥'), Suit('Spade', '♠')
        super().__init__(card2(i,j) for i in range(1,14) for j in [club, diamond, heart, spade])
        random.shuffle(self)


class Deck2(list):
    def __init__(self,decks=1):
        club, diamond, heart, spade = Suit('Club', '♣'), Suit('Diamond', '♦'), Suit('Heart', '♥'), Suit('Spade', '♠')
        super().__init__()
        for i in range(decks):
            self.extend(card2(i,j) for i in range(1,14) for j in [club, diamond, heart, spade])
        random.shuffle(self)
        #Burning one card
        self.pop()
        
def card3(rank,suit):
    class_,rankStr={1:(AceCard,'A'),11:(FaceCard,'J'),12:(FaceCard,'Q'),13:(FaceCard,'K')}.get(rank,(NumberCard,str(rank)))
    return class_(suit,rankStr)

def card4(rank,suit):
    partClass={1:partial(AceCard,'A'),11:partial(FaceCard,'J'),12:partial(FaceCard,'Q'),13:partial(FaceCard,'K')}.get(rank,partial(NumberCard,str(rank)))
    return partClass(suit)

def main():
    deck=Deck2()
    d1=deck.pop()
    print(d1.rank,d1.suit.symbol)
    # cards=[cardd.rank(i).suit(j) for i in range(1,14) for j in [club, diamond, heart, spade]]
    # for i in cards:
    #    print(i.suit.symbol,i.rank)

if __name__ == '__main__':
    main()
