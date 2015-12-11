# -*- coding: utf-8 -*-

import random


class SuitLike(str):

    SUITS = (u'♠', u'♥', u'♦', u'♣')

    def __init__(self, suit=''):
        super(SuitLike, self).__init__()
        if len(suit) > 0:
            assert suit in SuitLike.SUITS


class RankLike(str):

    ACE_HIGH = True
    RANKS = (u'A', u'2', u'3', u'4', u'5', u'6', u'7', u'8', u'9', u'10', u'J', u'Q', u'K')
    VALUES = {'': 0, '1': 1, '2': 2, '3': 3, '4': '4', '5': 5, '6': 6, '7': 7, '8': 8,
              '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

    def __init__(self, rank=''):
        super(RankLike, self).__init__()
        self._high = RankLike.VALUES[rank]
        self._low = 1 if not RankLike.ACE_HIGH else self._high

    def __lt__(self, other):
        if isinstance(other, str):
            other = RankLike(other)
        return self.getvalue() < other.getvalue()

    def __int__(self):
        return self.getvalue()

    def getvalue(self, ace_high=ACE_HIGH):
        return self._high if ace_high else self._low

    def gethigh(self):
        return self._high

    def getlow(self):
        return self._low

    value = property(fget=getvalue, doc='gets the value for the rank')
    low = property(fget=getlow, doc='gets the low value for the rank')
    high = property(fget=gethigh, doc='gets the high value for the rank')


class CardLike(str):

    CARDS = tuple(''.join((s, r)) for r in RankLike.RANKS for s in SuitLike.SUITS)

    def __init__(self, card=''):
        super(CardLike, self).__init__()
        self._suit = None
        self._rank = None

    def __lt__(self, other):
        if isinstance(other, str):
            other = CardLike(other)
        return self.getrank().__lt__(other.getrank())

    def getsuit(self):
        if self._suit is None:
            if len(self) > 0:
                self._suit = SuitLike(self[0])
        return self._suit

    def getrank(self):
        if self._rank is None:
            if len(self) > 0:
                self._rank = RankLike(self[1:])
        return self._rank

    suit = property(fget=getsuit, doc='the suit of this card')
    rank = property(fget=getrank, doc='the rank of this card')


deck = tuple(map(CardLike, CardLike.CARDS))


def deal(source=None, discard=True, limit=None):
    if limit is None:
        limit = float('inf')
    if source is None:
        source = list(deck) if discard else deck
    i = 0
    while i < limit and len(source) > 0:
        r = random.randrange(len(source))
        yield source[r]
        if discard:
            del source[r]
        i += 1