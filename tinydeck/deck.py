# -*- coding: utf-8 -*-

import random


suits = ('♠', '♥', '♦', '♣')
ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K', '10')
deck = tuple(''.join((s, r)) for r in ranks for s in suits)


def deal(source=None, discard=True, limit=None, rand=random):
    if limit is None:
        limit = float('inf')
    if source is None:
        source = list(deck) if discard else deck
    i = 0
    while i < limit and len(source) > 0:
        r = rand.randrange(len(source))
        yield source[r]
        if discard:
            del source[r]
        i += 1
